from fastapi import FastAPI, Body, Request
from fastapi.responses import JSONResponse

from pydantic import BaseModel, Field

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

class NegativeIdException(Exception):
    def __init__(self, message: str):
        self.message = message


@app.exception_handler(NegativeIdException)
async def negative_id_exception_handler(request: Request, exc: NegativeIdException):
    return JSONResponse(
        status_code=418,
        content={"message": f"{exc.message}"},
    )


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    if user_id < 0:
        raise NegativeIdException(message=f"Invalid user id {user_id}")
    return user

