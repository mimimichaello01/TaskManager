from src.app.infrastructure.repositories.task_repositori_impl import TaskRepositoryImpl
from src.app.infrastructure.service.interfaces.task_service import TaskService

from typing import Optional, List

from src.app.core.task_entity import Task

class TaskServiceImpl(TaskService):
    def __init__(self, task_repo: TaskRepositoryImpl):
        self.task_repo = task_repo

    def get_task(self, task_id: int) -> Optional[Task]:
        task = self.task_repo.get_task(task_id)
        if not task:
            raise ValueError("The issue was not found")

        return task

    def get_all_tasks(self) -> List[Task]:
        return self.task_repo.get_all_tasks()

    def add_task(self, task: Task) -> Task:
        return self.task_repo.add_task(task)

    def update_task(self, task_id: int, task: Task) -> Optional[Task]:
        updated = self.task_repo.update_task(task_id, task)
        if not updated:
            raise ValueError(f"Task with id {task_id} not found")
        return updated

    def delete_task(self, task_id: int):
        return self.task_repo.delete_task(task_id)
