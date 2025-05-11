from abc import ABC, abstractmethod
from typing import Optional, List

from src.app.core.task_entity import Task


class TaskService(ABC):

    @abstractmethod
    def get_task(self, task_id: int) -> Optional[Task]:
        """Получить задачу по ID. Возвращает сущность Task или None."""
        pass

    @abstractmethod
    def get_all_tasks(self) -> List[Task]:
        """Получить все задачи. Возвращает список Task."""
        pass

    @abstractmethod
    def add_task(self, task: Task) -> Task:
        """Добавить новую задачу. Принимает и возвращает сущность Task."""
        pass

    @abstractmethod
    def update_task(self, task_id: int, task: Task) -> Optional[Task]:
        """Обновить задачу. Принимает и возвращает сущность Task."""
        pass

    @abstractmethod
    def delete_task(self, task_id: int) -> None:
        """Удалить задачу по ID."""
        pass
