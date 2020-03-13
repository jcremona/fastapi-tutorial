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

# The function parameters will be recognized as follows:
#
# -If the parameter is also declared in the path, it will be used as a path parameter.
# -If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.
# -If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.


def update_db(user_id, user):
    print(user_id)