from pydantic import BaseModel

class ToDoBase(BaseModel):
    title: str
    description: str
    completed: bool = False

class ToDoCreate(ToDoBase):
    pass

class ToDo(ToDoBase):
    id: int

    class Config:
        orm_mode = True
