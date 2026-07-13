from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional
from fastapi.exceptions import HTTPException

app = FastAPI()

students = [
    {
        "id" : 1,
        "name" : "Chirag Mittal",
        "age" : 22,
        "Education" : "B.Tech Graduate",
        "More" : "Waiting for joining" 
    },
    {
        "id" : 2,
        "name" : "Vansh Tyagi",
        "age" : 22,
        "Education" : "B.Tech Graduate",
        "More" : "Applying in companies"
    },
    {
        "id" : 3,
        "name" : "Punit Jatrana",
        "age" : 22,
        "Education" : "B.Tech Graduate",
        "More" : "Placed with a salary of 15,000"
    },
    {
        "id" : 4,
        "name" : "Anuprash Gautam",
        "age" : 23,
        "Education" : "B.Tech Graduate",
        "More" : "Placed with a good package"
    },
    {
        "id" : 5,
        "name" : "Rachit Deshwal",
        "age" : 23,
        "Education" : "B.Tech Graduate, Married",
        "More" : "Applying in companies, Struggling to get job"
    }
]

class user(BaseModel):
    id:int
    name:str
    age:int
    education:str
    More:str

@app.get("/")
def root():
    return {"message" : "Welcome to home page"}

@app.get("/student")
def get_all():
    return students

@app.get("/student/{id}")
def get_by_id(id:int):
    for user in students:
        if user['id'] == id:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.post("/students")
def add_user(student:user):
    new_user = student.model_dump()
    students.append(new_user)
    return students

class userUpdate(BaseModel):
    More:str

@app.put("/students/{id}")
def user_info_update(id:int, update:userUpdate):
    for user in students:
        if user['id'] == id:
            user['More'] = update.More
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@app.delete("/students/{id}")
def delete_user(id:int):
    for user in students:
        if user['id'] == id:
            students.remove(user)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return students