from fastapi import FastAPI
from backend.routes import router as task_router
from backend.models import Base
from backend.database import engine
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(title="Task Manager API", lifespan=lifespan)
app.include_router(task_router)
