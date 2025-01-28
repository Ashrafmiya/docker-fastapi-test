from fastapi import FastAPI, HTTPException
from app import services
from app.schema import UserIn, BaseResponse, UserListOut

app = FastAPI()

@app.get("/")
async def index():
    """
    Index route for our application
    """
    return {"message": "Hello from FastAPI ;)"}

@app.post("/users", response_model=BaseResponse, status_code=201)
async def user_create(user: UserIn):
    """
    Add user data to JSON file
    """
    try:
        services.add_userdata(user.model_dump())  # Correct Pydantic v2 method
        return {"success": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users", response_model=UserListOut)
async def get_users():
    """
    Read user data from JSON file
    """
    users = services.read_usersdata()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users
