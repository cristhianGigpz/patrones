from fastapi import FastAPI

app = FastAPI()


@app.get("/orders")
def get_orders():
    return [{"id": 101, "product_id": 1}, {"id": 102, "product_id": 2}]


# uv run uvicorn orders:app --port 8003
