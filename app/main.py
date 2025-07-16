from fastapi import FastAPI
from app.api import todos
from app.db import database

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(todos.router)

@app.get("/")
def read_root():
    return {"message": "API is up and running!"}
