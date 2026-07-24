# User Response Model
# Hiding sensitive data from client

from fastapi import FastAPI
from pydantic import BaseModel

class userCreate(BaseModel):
    id : int
    name : str
    email : str
    password : str
class userResponse(BaseModel):
    id : int
    name : str
    email : str

app = FastAPI()

@app.post("/user", response_model=userResponse)
def create(user:userCreate):
    return {
        "id" : user.id,
        "name" : user.name,
        "email" : user.email,
        "pass" : user.password
    }
