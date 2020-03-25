from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(*, session_id: str = Cookie(None)): # Try adding alias="session-id"
    return {"session_id": session_id}