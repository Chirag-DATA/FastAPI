from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

todos =[]

class ToDo(BaseModel):
    id : int
    title : str
    completed : bool

app = FastAPI()

@app.get("/")
def get_all():
    return todos

@app.post("/todos")
def create_todo(todo:ToDo):
    todos.append(todo)
    return {
            "message" : "ToDo created",
            "data" : todo
        }

@app.get("/todos/{todo_id}")
def get_by_id(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ToDo Not Found")

@app.put("/todos/{todo_id}")
def update(todo_id:int, updated_todo:ToDo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {
                "message" : "Updated Data",
                "data" : todos
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.delete("/todos/{todo_id}")
def del_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {
                "message" : "Deleted"
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)