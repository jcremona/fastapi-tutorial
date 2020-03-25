from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import List

class User(BaseModel):
    name: str
    age: int = Field(..., gt=0, description="The age must be greater than zero")

app = FastAPI()

# Path params + request body
@app.put("/users/{user_id}")
async def update_user(user_id, user: User):
    return user

