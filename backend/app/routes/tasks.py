import asyncio

from fastapi import APIRouter, HTTPException

from app.schemas import TaskCreateRequest, TaskResponse, TaskReviewRequest
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])
task_service = TaskService()
running_tasks: set[asyncio.Task[None]] = set()


async def _execute_task(task_id: str) -> None:
    try:
        await task_service.execute_task(task_id)
    except Exception as exc:  # pragma: no cover - defensive failure path
        await task_service.fail_task(task_id, str(exc))


@router.get("", response_model=list[TaskResponse])
def list_tasks() -> list[TaskResponse]:
    return task_service.list_tasks()


@router.post("", response_model=TaskResponse, status_code=201)
async def create_task(payload: TaskCreateRequest) -> TaskResponse:
    task = task_service.create_task(payload)
    background_task = asyncio.create_task(_execute_task(task.task_id))
    running_tasks.add(background_task)
    background_task.add_done_callback(running_tasks.discard)
    return task


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: str) -> TaskResponse:
    try:
        return task_service.get_task(task_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Task not found") from exc


@router.post("/{task_id}/review", response_model=TaskResponse)
async def review_task(task_id: str, payload: TaskReviewRequest) -> TaskResponse:
    try:
        return await task_service.review_task(task_id, payload)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Task not found") from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
