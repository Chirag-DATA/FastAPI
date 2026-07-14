from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional
from fastapi.exceptions import HTTPException

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Atomic Habits",
        "author": "James Clear",
        "genre": "Self Help",
        "price": 499,
        "rating": 4.8,
        "published_year": 2018,
        "available": True
    },
    {
        "id": 2,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "genre": "Fiction",
        "price": 350,
        "rating": 4.6,
        "published_year": 1988,
        "available": True
    },
    {
        "id": 3,
        "title": "Rich Dad Poor Dad",
        "author": "Robert T. Kiyosaki",
        "genre": "Finance",
        "price": 450,
        "rating": 4.7,
        "published_year": 1997,
        "available": False
    },
    {
        "id": 4,
        "title": "Deep Work",
        "author": "Cal Newport",
        "genre": "Productivity",
        "price": 550,
        "rating": 4.5,
        "published_year": 2016,
        "available": True
    },
    {
        "id": 5,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "genre": "Programming",
        "price": 799,
        "rating": 4.9,
        "published_year": 2008,
        "available": True
    },
    {
        "id": 6,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "genre": "Programming",
        "price": 899,
        "rating": 4.8,
        "published_year": 2019,
        "available": True
    },
    {
        "id": 7,
        "title": "The Psychology of Money",
        "author": "Morgan Housel",
        "genre": "Finance",
        "price": 420,
        "rating": 4.8,
        "published_year": 2020,
        "available": False
    },
    {
        "id": 8,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "genre": "Programming",
        "price": 950,
        "rating": 4.9,
        "published_year": 1999,
        "available": True
    },
    {
        "id": 9,
        "title": "Ikigai",
        "author": "Hector Garcia",
        "genre": "Lifestyle",
        "price": 399,
        "rating": 4.4,
        "published_year": 2016,
        "available": True
    },
    {
        "id": 10,
        "title": "Zero to One",
        "author": "Peter Thiel",
        "genre": "Business",
        "price": 499,
        "rating": 4.5,
        "published_year": 2014,
        "available": False
    }
]

#---------------GET Request-----------------------------

@app.get("/")
def root():
    return {"message" : "Home Page"}

@app.get("/book")
def get_all():
    return books

@app.get("/book/{id}")
def get_id(id:int):
    for book in books:
        if book['id'] == id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/cheap")
def get_cheap_books():
    cheap_books = []
    
    for book in books:
        if book["price"] < 500:
            cheap_books.append(book)
        
    return cheap_books

@app.get("/books/available")
def get_available_books():
    avail_books = []
    for book in books:
        if book["available"]:
            avail_books.append(book)
    return avail_books

#----------------------- POST Request ----------------------

class Book(BaseModel):
    id : int
    title : str
    author : str
    genre : str
    price : int
    rating : float
    published_year : int
    available : Optional[bool] = True

@app.post("/books/add")
def add_book(book:Book):
    new_book = book.model_dump()
    books.append(new_book)
    return {
        "message" : "Book added successfully",
        "book" : books
    }

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):

    for index, book in enumerate(books):
        if book["id"] == book_id:
            books[index] = updated_book.model_dump()
            return {
                "message": "Book updated successfully",
                "book": books[index]
            }

    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/book/{id}")
def delete_book(id:int):
    for book in books:
        if book['id'] == id:
            books.remove(book)
    return {
        "message" : "Deleted Successfully",
        "Books" : books
    }