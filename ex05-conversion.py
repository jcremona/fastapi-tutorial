from fastapi import FastAPI

app = FastAPI()

USERS = [{"name": "user1"},
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
@app.get("/users/")
async def get_users(maxlength: int = 5, verbose: bool = False): # Try different values for verbose: on, off, yes, no.
    response = {"users": USERS[:maxlength]}
    if verbose:
        response.update({"description": "This a list of users"})
    return response
