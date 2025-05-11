from pydantic import BaseModel


class Task(BaseModel):
    title: str
    is_completed: bool

    class Config:
        from_attributes = True
