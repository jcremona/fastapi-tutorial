from fastapi import FastAPI, Response

app = FastAPI()


@app.post("/setcookie/")
def set_cookie(response: Response):
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return {"message": "We have set a response cookie."}