from pydantic import BaseModel

class todo_schema(BaseModel):

    id : int
    task : str
    completed : str
