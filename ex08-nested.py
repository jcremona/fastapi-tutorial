from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from typing import List

class Image(BaseModel):
    url: HttpUrl          # Try using HttpUrl
    name: str

class User(BaseModel):
    name: str
    age: int
    tags: List[str] = []
    photo: Image = None

app = FastAPI()


# Path params + request body
@app.put("/users/{user_id}")
async def update_user(user_id, user: User):
    update_db(user_id, user)
    return user

def update_db(user_id, user):
    print(user_id)