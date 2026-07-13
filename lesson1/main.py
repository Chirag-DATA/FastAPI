from fastapi import FastAPI

app = FastAPI()


@app.get("/students")
def get_students():
    return {"operation": "Fetch Students"}


@app.post("/students")
def create_student():
    return {"operation": "Student Created"}

@app.put("/students")
def update_student():
    return {"operation": "Student Updated"}

@app.delete("/students")
def delete_student():
    return {"operation": "Student Deleted"}