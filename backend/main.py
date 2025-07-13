from fastapi import FastAPI
from backend.routes import router as task_router
from backend.models import Base
from backend.database import engine

app = FastAPI(title="Task Manager API")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(task_router)
