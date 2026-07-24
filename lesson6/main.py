from fastapi import FastAPI
from pydantic import BaseModel

class user(BaseModel):
    name : str
    age : int

app = FastAPI()

@app.post("/user")
def create_user(user:dict):                  #normal --> no data validation
    return {
        "message" : "User Created",
        "data" : user
    }

@app.post("/users")
def create(user:user):                      #using pydantic --> data validation using user class
    return user                            