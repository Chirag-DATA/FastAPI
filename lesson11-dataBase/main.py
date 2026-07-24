from fastapi import FastAPI, Depends
from database import engine, SessionLocal
from sqlalchemy.orm import Session 
import model
import schema

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/new")
def add_task(
    todos : schema.todo_schema,
    db: Session = Depends(get_db)):

    new = model.todo(
        id=todos.id,
        task=todos.task,
        completed=todos.completed
    )
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@app.get("/task")
def get_all(db:Session=Depends(get_db)):
    return db.query(model.todo).all()

@app.get("/task/{id}")
def get_id(db : Session=Depends(get_db), id=int):
    task = (db.query(model.todo).filter(model.todo.id==id).first())
    if task:
        return task

    return "Not Exist"

@app.put("/update")
def change(todos : schema.todo_schema,
           db:Session=Depends(get_db), id=int):
    updated = db.query(model.todo).filter(model.todo.id==id).first()
    if updated:
        updated.id = id
        updated.task = todos.task
        updated.completed = todos.completed
        db.commit()
        return "updated"
    return "Not exist"

@app.delete("/del/{id}")
def delete(id:int, db:Session=Depends(get_db)):
    toDel = db.query(model.todo).filter(model.todo.id==id).first()
    if toDel:
        db.delete(toDel)
        db.commit()
        return "Deleted Successfully"
    return "Not Exist"

    