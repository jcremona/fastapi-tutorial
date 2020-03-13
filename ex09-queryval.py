from fastapi import FastAPI, Query

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
async def get_users(maxlength: int = Query(5, gt=0, le=10)): # Try deleting the default value and set ...
    return USERS[:maxlength]

# Try using alias.