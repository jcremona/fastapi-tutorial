from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import List

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

# Path params + request body + request body using Body
@app.put("/users/{user_id}")
async def update_user(user_id, user: User, level: int = Body(..., gt=2)):
    update_db(user_id, level, user)
    return user

def update_db(user_id, level, user):
    print(f"User id: {user_id}")
    print(f"Level: {level}")