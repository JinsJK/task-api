from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from backend.routes import router as task_router
from backend.models import Base
from backend.database import engine
import traceback
import sys

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    except Exception as e:
        print("🚨 DB init failed:", file=sys.stderr)
        traceback.print_exc()  # <== this is key
    yield

app = FastAPI(title="Task Manager API", lifespan=lifespan)

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

app.include_router(task_router)
