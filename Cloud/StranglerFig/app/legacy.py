from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
def get_users():
    return {"source": "legacy", "users": ["Ana", "Luis"]}


@app.get("/products")
def get_products():
    return {"source": "legacy", "products": ["Laptop"]}
