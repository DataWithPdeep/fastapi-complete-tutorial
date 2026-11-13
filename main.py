from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def home():
    return {"messages": "Welcome to FastAPI"}


@app.get("/about")
def about():
    return {"message":"This is about Page"}

#user Route
@app.get("/users")
def get_user(name: str =None):
    return {"Name":name}

@app.get("/products")
def get_user(limit: int =10):
    return {"limit":limit}

@app.get("/item")
def get_user(name:str = None, price: int=0):
    return {
        "name":name,
        "price":price

    }


class User(BaseModel):
    name:str
    age:int

@app.post("/create-user")
def create_user(user:User):
    return{
        "message":"User Created",
        "data":user
    }

class Address(BaseModel):
    city:str
    pincode:int

class Users(BaseModel):
    name:str
    age:int
    email:str
    adress:Address

@app.post("/create-users")
def create_user(user:Users):
    return {
        "message":"User Created",
        "data":user
    }











