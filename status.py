from fastapi import FastAPI, status,HTTPException
from pydantic import BaseModel


app = FastAPI()

@app.post("/create_user", status_code=status.HTTP_201_CREATED)
def create_uesr():
    return{
        "message":"User Created"
    }

@app.get("/user")
def get_user():
    return{
        "status":"Success",
        "message":"User Fatched",
        "data":{
            "name":"Mohit",
            "age":35

        }
    }

@app.get("/users/{user_id}")
def get_user(user_id):
    if user_id !=1:
        raise HTTPException(
            status_code=404,
            detail="Used Not  Found"
        )
    return{
        "id":1,
        "name":"Mohit"
    }

