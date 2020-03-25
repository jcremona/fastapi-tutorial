from fastapi import FastAPI, Header

app = FastAPI()

# https://github.com/tiangolo/fastapi/blob/master/fastapi/params.py

@app.get("/items/")
async def read_items(*, user_agent: str = Header(None), host:str = Header(None)):
    return {"Host": host, "User-Agent": user_agent}