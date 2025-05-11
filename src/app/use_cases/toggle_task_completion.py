from src.app.core.task_entity import Task
from src.app.infrastructure.service.interfaces.task_service import TaskService


class ToggleTaskCompletion:
    def __init__(self, service: TaskService):
        self.service = service

    def execute(self, task_id: int) -> Task:
        task = self.service.get_task(task_id)
        task.is_completed = not task.is_completed
        return self.service.update_task(task_id, task)
