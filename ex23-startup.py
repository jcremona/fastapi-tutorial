from fastapi import FastAPI

app = FastAPI()

items = {}

# To add a function that should be run before the application starts,
# declare it with the event "startup"
@app.on_event("startup")
async def startup_event():
    items["foo"] = {"name": "Fighters"}
    items["bar"] = {"name": "Tenders"}


@app.get("/items/{item_id}")
async def read_items(item_id: str):
    return items[item_id]