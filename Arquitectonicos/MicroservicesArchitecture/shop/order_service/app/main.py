from fastapi import FastAPI, HTTPException

from .orders import create_order

app = FastAPI()


@app.post("/orders/{product_id}")
def new_order(product_id: int):

    order = create_order(product_id)

    if order is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return order


## uv init
## uv add fastapi uvicorn
## uv run uvicorn app.main:app --port 8002 --reload
