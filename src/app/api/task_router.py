from fastapi import APIRouter, Depends, HTTPException

from src.app.use_cases.toggle_task_completion import ToggleTaskCompletion
from src.app.api.dependencies import get_task_service
from src.app.api.schemas import Task
from src.app.infrastructure.service.interfaces.task_service import TaskService


task_router = APIRouter(prefix='/tasks', tags=['tasks'])


@task_router.get('/{task_id}', response_model=Task)
def get_task(task_id: int, service: TaskService = Depends(get_task_service)):
    return service.get_task(task_id)


@task_router.get("/", response_model=list[Task])
def get_all_tasks(service: TaskService = Depends(get_task_service)):
    return service.get_all_tasks()

@task_router.post("/", response_model=Task)
def create_task(task: Task, service: TaskService = Depends(get_task_service)):
    return service.add_task(task)


@task_router.patch("/{task_id}/toggle-completion", response_model=Task)
def toggle_task_completion(
    task_id: int,
    task_service: TaskService = Depends(get_task_service)
):
    toggle_task_use_case = ToggleTaskCompletion(service=task_service)
    task = toggle_task_use_case.execute(task_id)
    return task
