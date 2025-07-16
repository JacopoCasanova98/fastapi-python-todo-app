from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.todos import get_todo, get_todos, create_todo, update_todo, delete_todo
from app.schemas.todo import ToDo, ToDoCreate
from app.db.database import get_db

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)

@router.post("/", response_model=ToDo)
def create(todo: ToDoCreate, db: Session = Depends(get_db)):
    return create_todo(db=db, todo=todo)

@router.get("/", response_model=list[ToDo])
def read(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_todos(db, skip=skip, limit=limit)

@router.get("/{todo_id}", response_model=ToDo)
def read_one(todo_id: int, db: Session = Depends(get_db)):
    db_todo = get_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return db_todo

@router.put("/{todo_id}", response_model=ToDo)
def update(todo_id: int, todo: ToDoCreate, db: Session = Depends(get_db)):
    db_todo = update_todo(db, todo_id, todo)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return db_todo

@router.delete("/{todo_id}", response_model=ToDo)
def delete(todo_id: int, db: Session = Depends(get_db)):
    db_todo = delete_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return db_todo
