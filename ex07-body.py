from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


app = FastAPI()


# Request body
@app.post("/users/")
async def create_user(user: User):
    return user

# Path params + request body
@app.put("/users/{user_id}")
async def update_user(user_id, user: User):
    update_db(user_id, user)
    return user

def update_db(user_id, user):
    print(user_id)