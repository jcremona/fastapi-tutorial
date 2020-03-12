from fastapi import FastAPI

app = FastAPI()

USERS = [{"name": "user0"},
         {"name": "user1"},
         {"name": "user2"},
         {"name": "user3"},
         {"name": "user4"},
         {"name": "user5"},
         {"name": "user6"},
         {"name": "user7"},
         {"name": "user8"},
         {"name": "user9"},
         {"name": "user10"},
         ]


# When you declare other parameters that are not part of the path parameters,
# they are automatically interpreted as "query" parameters
@app.get("/users/{user_id}")
async def get_user(user_id: int, verbose: bool = False): # Try different values for verbose: on, off, yes, no.
    response = {"user": USERS[user_id]}
    if verbose:
        response.update({"description": "This a specific user"})
    return response
