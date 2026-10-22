from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
def get_users():
    return [{"id": 1, "name": "Ana"}, {"id": 2, "name": "Carlos"}]


# uv run uvicorn users:app --port 8001
