from sqlalchemy.orm import Session

from src.app.core.task_entity import Task
from src.app.infrastructure.db.models import TaskModel
from src.app.infrastructure.repositories.interfaces.task_repository import (
    AbstractTaskRepository,
)

from typing import Optional, List


class TaskRepositoryImpl(AbstractTaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def _entity_to_model(self, task: Task) -> TaskModel:
        return TaskModel(title=task.title, is_completed=task.is_completed)

    def _model_to_entity(self, task_model: TaskModel) -> Task:
        return Task(
            id=task_model.id,
            title=task_model.title,
            is_completed=task_model.is_completed,
        )

    def get_task(self, task_id) -> Optional[Task]:
        task_model = self.db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if task_model:
            return self._model_to_entity(task_model)
        return None

    def get_all_tasks(self) -> List[Task]:
        tasks = self.db.query(TaskModel).all()
        if tasks:
            return [self._model_to_entity(task) for task in tasks]
        return []

    def add_task(self, task: Task) -> Task:
        task_model = self._entity_to_model(task)
        self.db.add(task_model)
        self.db.commit()
        self.db.refresh(task_model)
        return self._model_to_entity(task_model)

    def update_task(self, task_id: int, task: Task) -> Optional[Task]:
        task_model = self.db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if not task_model:
            return None

        task_model.title = task.title
        task_model.is_completed = task.is_completed
        self.db.commit()
        self.db.refresh(task_model)

        return self._model_to_entity(task_model)

    def delete_task(self, task_id: int) -> None:
        self.db.query(TaskModel).filter(TaskModel.id == task_id).delete()
        self.db.commit()
        return None
