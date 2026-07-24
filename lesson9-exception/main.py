from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi import exception_handlers

app = FastAPI()

products = {
    1: "Laptop",
    2: "Mouse"
}

class ProductNotFoundException(Exception):
    def __init__(self):
        self.message = "Product Not Found"

@app.exception_handler(ProductNotFoundException)
def product_exception_handler(
    request:Request,
    exc:ProductNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "error" : exc.message
        }
    )

@app.get("/products/{id}")
def get_product(id: int):

    if id not in products:
        raise ProductNotFoundException()

    return products[id]