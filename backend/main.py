from fastapi import FastAPI
from backend.routes import router as task_router

app = FastAPI(title="Task Manager API")

app.include_router(task_router)
