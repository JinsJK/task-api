from pydantic import BaseModel, ConfigDict

class TaskCreate(BaseModel):
    title: str

class TaskRead(TaskCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
