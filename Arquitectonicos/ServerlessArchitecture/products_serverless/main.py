from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from functions.get_product import handler as get_product_handler
from functions.create_product import handler as create_product_handler

app = FastAPI(title="Serverless Local Runner con FastAPI")


# Esquema para validar el cuerpo del POST de forma sencilla
class ProductSchema(BaseModel):
    name: str
    price: float


# Elimina la línea con el error y deja solo esto:


@app.get("/products/{product_id}")
def get_product(product_id: int):
    # Mimic del objeto 'event' que espera tu get_product.py
    event = {"pathParameters": {"id": str(product_id)}}
    context = {}

    response = get_product_handler(event, context)

    if response["statusCode"] == 404:
        raise HTTPException(status_code=404, detail=response["body"])

    return response["body"]


@app.post("/products", status_code=201)
def create_product(product: ProductSchema):
    # Mimic del objeto 'event' que espera tu create_product.py
    event = {
        "body": product.model_dump()  # Convierte el modelo Pydantic a diccionario de Python
    }
    context = {}

    response = create_product_handler(event, context)
    return response["body"]


## uv init
## uv add fastapi uvicorn pydantic
## uv run uvicorn main:app --reload

"""
{
    "name": "Keyboard",
    "price": 150
}
"""
