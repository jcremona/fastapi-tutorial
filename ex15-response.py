from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: List[str] = []

class ItemOut(BaseModel):
    name: str
    description: str = None


@app.post("/items/", response_model=ItemOut) # Try using Item and response_model_include={"name", "description"}
async def create_item(item: Item):
    # FastAPI will take care of filtering out all the data
    # that is not declared in the output model
    return item