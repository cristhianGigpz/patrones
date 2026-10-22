from fastapi import FastAPI

app = FastAPI()


@app.get("/products")
def get_products():
    return [{"id": 1, "name": "Laptop"}, {"id": 2, "name": "Mouse"}]


# uv run uvicorn products:app --port 8002
