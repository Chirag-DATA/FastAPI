from database import Base
from sqlalchemy import Column, Integer, String

class todo(Base):
    __tablename__ = "ToDo"
    id = Column(Integer, primary_key=True, index=True)
    task= Column(String)
    completed = Column(String)


