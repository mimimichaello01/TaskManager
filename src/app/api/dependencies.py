from fastapi import Depends

from src.app.infrastructure.db.session import get_db

from src.app.infrastructure.repositories.task_repositori_impl import TaskRepositoryImpl
from src.app.infrastructure.service.task_service_impl import TaskServiceImpl

def get_task_service(db = Depends(get_db)):
    repo = TaskRepositoryImpl(db)
    return TaskServiceImpl(repo)
