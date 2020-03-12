from enum import Enum

from fastapi import FastAPI


class ColorName(str, Enum):
    red = "red"
    green = "green"
    yellow = "yellow"


app = FastAPI()

@app.get("/color/{color_name}")
async def select_color(color_name: ColorName): # Try deleting the type
    if color_name == ColorName.red:
        return {"message": "Red Light. You must stop!"}
    elif color_name == ColorName.yellow:
        return {"message": "Yellow Light. Warning!"}
    else:
        return {"message": "Green Light. Now you can pass!"}
