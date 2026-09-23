from fastapi import FastAPI, HTTPException

app = FastAPI()

products = {1: {"name": "Laptop", "price": 2000}, 2: {"name": "Mouse", "price": 100}}


@app.get("/products/{product_id}")
def get_product(product_id: int):

    product = products.get(product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return product


## uv init
## uv add fastapi uvicorn requests
## uv run uvicorn products:app --port 8001 --reload
