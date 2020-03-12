from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()

# The instance is referenced here to set the url path. Try change the instance's name.
@app.get("/")
async def root():
    return {"message": "Hello World"}