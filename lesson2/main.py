from fastapi import FastAPI

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

@app.get("/")
def home():
    return {"message" : "here on home page"}


@app.get("/students/{id}")
def get_id(id : int):
    return students[id] 