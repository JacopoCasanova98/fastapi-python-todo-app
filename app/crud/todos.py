from sqlalchemy.orm import Session
from app.models.todo import ToDo
from app.schemas.todo import ToDoCreate

def get_todos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ToDo).offset(skip).limit(limit).all()

def get_todo(db: Session, todo_id: int):
    return db.query(ToDo).filter(ToDo.id == todo_id).first()

def create_todo(db: Session, todo: ToDoCreate):
    db_todo = ToDo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo: ToDoCreate):
    db_todo = get_todo(db, todo_id)
    if db_todo:
        db_todo.title = todo.title
        db_todo.description = todo.description
        db_todo.completed = todo.completed
        db.commit()
        db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = get_todo(db, todo_id)
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo
