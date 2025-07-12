from fastapi import APIRouter
from backend.models import Task

router = APIRouter()

# Fake in-memory DB
tasks = [
    Task(id=1, title="Do homework"),
    Task(id=2, title="Read a book")
]

@router.get("/tasks", response_model=list[Task])
def read_tasks():
    return tasks

@router.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task
