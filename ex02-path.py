from fastapi import FastAPI

app = FastAPI()

# We can declare path parameters
@app.get("/users/{user_id}")
async def read_user(user_id): # Try adding a type!
    return {"user_id": user_id}

# Try having a fixed path
# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}