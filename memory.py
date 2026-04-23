from pydantic import BaseModel
import uuid
import time


class Memory(BaseModel):
    id = uuid.uuid4()
    content: str
    embedding: str
    timestamp: time.now()
    importance: str
