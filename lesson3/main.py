from fastapi import FastAPI

app = FastAPI()

@app.get("/employee/{id}")
def get_emp(id:int):
    return {
        "Employee" : id
    }

@app.get("/employee/")
def get_detail(dep:str,exp:int = 0):
    return {
        "Department" : dep,
        "Experience" : exp
    }

@app.get("/employee/{emp_id}/projects/{proj_id}")
def get_id(emp_id:int,proj_id:int):
    return {
        "EmployeeID" : emp_id,
        "ProjectID" : proj_id
    }