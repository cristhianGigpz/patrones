from fastapi import FastAPI, HTTPException

from .products import find_product

app = FastAPI()


@app.get("/products/{product_id}")
def get_product(product_id: int):

    product = find_product(product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return product


## uv init
## uv add fastapi uvicorn
## uv run uvicorn app.main:app --port 8001 --reload
