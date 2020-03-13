from fastapi import FastAPI, Path

app = FastAPI()

# We can declare path parameters
@app.get("/users/{user_id}")
async def read_user(user_id: str = Path(..., regex="usr[0-9]+")): # Try adding max_length
    return {"user_id": user_id}
