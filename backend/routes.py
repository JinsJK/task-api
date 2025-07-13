from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from backend.models import Task
from backend.database import get_db
from backend.schemas import TaskCreate, TaskRead

router = APIRouter()

@router.get("/tasks", response_model=list[TaskRead])
async def read_tasks(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task))
    tasks = result.scalars().all()
    return tasks

@router.post("/tasks", response_model=TaskRead)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    new_task = Task(title=task.title)
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task
