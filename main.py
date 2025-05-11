from fastapi import FastAPI

from src.app.api.task_router import task_router

app = FastAPI()
app.include_router(task_router)
