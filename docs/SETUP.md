# Setup Guide

This guide explains how to prepare and run SovereignAI Workbench locally and with Docker.

## 1. Prerequisites

### Required

- Git
- Python 3.10 or newer
- Node.js 20 or newer and npm
- Docker 24+ and Docker Compose
- 16 GB RAM minimum for development
- 50 GB free disk space, excluding model files

### Optional

- NVIDIA GPU and compatible container runtime
- Local OCR engine such as Tesseract
- Local model runtime such as Ollama or llama.cpp

The starter application runs in mock/offline mode and does not require a live LLM service.

## 2. Clone the repository

```bash
git clone https://github.com/jeevanhs06/SIH2026-MRPL-SovereignAI-Workbench.git
cd SIH2026-MRPL-SovereignAI-Workbench
```

## 3. Configure environment variables

```bash
cp .env.example .env
```

Important settings:

```env
OFFLINE_MODE=true
ALLOW_EXTERNAL_NETWORK=false
MODEL_RUNTIME=mock
```

Never commit `.env`, secrets, confidential documents, model weights, or generated private outputs.

## 4. Run with Docker Compose

```bash
docker compose up --build
```

Check service status:

```bash
docker compose ps
curl http://127.0.0.1:8000/health
```

Stop services:

```bash
docker compose down
```

The frontend and backend ports are defined in `docker-compose.yml`. Open the frontend URL shown by Docker and use the backend API documentation at `/docs`.

## 5. Run the backend locally

```bash
cd backend
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows PowerShell
# .venv\\Scripts\\Activate.ps1

pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt

uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Verify:

```bash
curl http://127.0.0.1:8000/health
```

## 6. Run the frontend locally

In another terminal:

```bash
cd frontend
npm install
npm run dev
```

The Vite development server normally runs at `http://127.0.0.1:5173`.

## 7. Prepare the knowledge base

Use only synthetic or publicly shareable files during development:

```text
knowledge_base/manuals/
knowledge_base/sops/
knowledge_base/templates/
knowledge_base/sample_documents/
```

Run the ingestion script when available:

```bash
python scripts/ingest_knowledge.py
```

The starter implementation uses a local placeholder/indexing path. Replace it with FAISS, Chroma, or another approved local vector store in a later milestone.

## 8. Optional OCR setup

Install Tesseract using your operating system package manager, then verify:

```bash
tesseract --version
```

OCR and vision adapters are intentionally isolated so the application can run without a model or OCR service during initial development.

## 9. Optional local model setup

Prepare model files before the offline demo. Record the model name, version, source, license, checksum, hardware requirements, and context length in `docs/MODELS.md`.

Do not download models automatically from application startup. The application must remain usable in mock mode.

## 10. Test the project

Backend:

```bash
cd backend
pytest -q
```

Frontend:

```bash
cd frontend
npm run build
npm run test
```

Repository scripts:

```bash
bash scripts/run_tests.sh
bash scripts/verify_offline_mode.sh
```

Run only commands that exist in the current implementation; update this document whenever scripts change.

## 11. Development workflow

1. Create a feature branch.
2. Update `.env` locally if needed.
3. Implement a small change.
4. Add tests and documentation.
5. Run backend tests and frontend build.
6. Check for secrets and confidential files.
7. Open a pull request.

Suggested branches:

```text
feature/document-ingestion
feature/knowledge-retrieval
feature/agent-workflow
feature/frontend-dashboard
feature/offline-security
```

## 12. Troubleshooting

### Port already in use

Find and stop the process using the configured port, or change the port in `.env` and the compose configuration.

### Docker build fails

Check Docker is running, remove stale images if necessary, and rebuild:

```bash
docker compose build --no-cache
docker compose up
```

### Model unavailable

Confirm the project is configured for `MODEL_RUNTIME=mock`, or verify the local model service and endpoint. The application must not silently fall back to an external provider.

### Permission errors in data directories

Ensure the application user can write to `data/inputs`, `data/outputs`, `data/tmp`, and `data/audit`.

## 13. Offline rehearsal

Before the SIH demo:

1. Prepare all dependencies and model files.
2. Disconnect or block outbound network access.
3. Set `OFFLINE_MODE=true`.
4. Run `scripts/verify_offline_mode.sh`.
5. Execute the complete demo workflow.
6. Save the logs and generated sample outputs.
7. Confirm the demo works without internet access.
