from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/items/", status_code=status.HTTP_201_CREATED) # or just 201
async def create_item(name: str):
    return {"name": name}

# Try:
# @app.post("/items/")
# async def create_item(name: str):
#     item = {"name": name}
#     return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)
