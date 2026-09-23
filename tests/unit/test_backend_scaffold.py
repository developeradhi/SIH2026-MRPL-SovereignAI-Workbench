import asyncio
import os
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

os.environ.setdefault("SOVAI_DATA_ROOT", str(Path("/tmp/sovereignai-data")))
os.environ.setdefault("SOVAI_INPUT_DIR", str(Path("/tmp/sovereignai-data/inputs")))
os.environ.setdefault("SOVAI_OUTPUT_DIR", str(Path("/tmp/sovereignai-data/outputs")))
os.environ.setdefault("SOVAI_TMP_DIR", str(Path("/tmp/sovereignai-data/tmp")))
os.environ.setdefault("SOVAI_VECTOR_STORE_DIR", str(Path("/tmp/sovereignai-data/vector_store")))
os.environ.setdefault("SOVAI_AUDIT_DIR", str(Path("/tmp/sovereignai-data/audit")))
os.environ.setdefault("SOVAI_MODEL_ENDPOINT", "http://127.0.0.1:11434")

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "backend"))

from app.main import app
from app.routes import tasks as task_routes
from app.services.storage import StorageService, StorageValidationError

client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_upload_extension_validation() -> None:
    response = client.post(
        "/documents/upload",
        files={"file": ("malicious.exe", b"not-allowed", "application/octet-stream")},
    )
    assert response.status_code == 400
    assert "not allowed" in response.json()["detail"]


def test_upload_read_is_capped_by_limit() -> None:
    storage = StorageService()

    class OversizedUpload:
        filename = "large.txt"

        def __init__(self) -> None:
            self.read_size: int | None = None

        async def read(self, size: int = -1) -> bytes:
            self.read_size = size
            return b"x" * (storage.settings.max_upload_size_bytes + 1)

    upload = OversizedUpload()
    with pytest.raises(StorageValidationError, match="exceeds configured size limit"):
        asyncio.run(storage.save_upload(upload))  # type: ignore[arg-type]

    assert upload.read_size == storage.settings.max_upload_size_bytes + 1


def test_path_traversal_is_blocked() -> None:
    storage = StorageService()
    outside_path = Path("/tmp/escape.txt")
    with pytest.raises(StorageValidationError):
        storage._ensure_within_inputs(outside_path)


def test_task_creation_and_execution_flow() -> None:
    response = client.post(
        "/tasks",
        json={
            "title": "Review inspection",
            "prompt": "Summarize key findings",
            "document_ids": [],
            "requires_review": True,
        },
    )
    assert response.status_code == 201
    task_id = response.json()["task_id"]

    async def wait_for_task() -> dict:
        for _ in range(30):
            state = client.get(f"/tasks/{task_id}")
            payload = state.json()
            if payload["status"] in {"waiting_for_review", "completed", "rejected", "failed"}:
                return payload
            await asyncio.sleep(0.05)
        return client.get(f"/tasks/{task_id}").json()

    payload = asyncio.run(wait_for_task())
    assert payload["status"] == "waiting_for_review"
    assert any(path.endswith("_result.json") for path in payload["output_files"])


def test_health_endpoint_supports_local_frontend_origin() -> None:
    response = client.options(
        "/health",
        headers={
            "Origin": "http://localhost:5173",
            "Access-Control-Request-Method": "GET",
        },
    )
    assert response.status_code == 200
    assert response.headers.get("access-control-allow-origin") == "http://localhost:5173"


def test_task_failure_is_supervised(monkeypatch: pytest.MonkeyPatch) -> None:
    async def crash(task_id: str) -> None:
        raise RuntimeError(f"boom:{task_id}")

    monkeypatch.setattr(task_routes.task_service, "execute_task", crash)

    response = client.post(
        "/tasks",
        json={
            "title": "Failing task",
            "prompt": "Force a failure",
            "document_ids": [],
            "requires_review": False,
        },
    )
    assert response.status_code == 201
    task_id = response.json()["task_id"]

    async def wait_for_failure() -> dict:
        for _ in range(30):
            payload = client.get(f"/tasks/{task_id}").json()
            if payload["status"] == "failed":
                return payload
            await asyncio.sleep(0.05)
        return client.get(f"/tasks/{task_id}").json()

    payload = asyncio.run(wait_for_failure())
    assert payload["status"] == "failed"
    assert any(event["event"] == "task_failed" for event in payload["events"])


def test_offline_network_status() -> None:
    response = client.get("/security/network-status")
    assert response.status_code == 200
    body = response.json()
    assert body["offline_mode"] is True
    assert body["model_endpoint_local"] is True
    assert "host firewall proof" in body["note"].lower()


def test_knowledge_ingestion_rejects_invalid_collection() -> None:
    response = client.post("/knowledge/ingest", json={"collection": "../tmp"})
    assert response.status_code == 422
