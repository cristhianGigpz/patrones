import sqlite3
import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI()

USER_SERVICE = "http://localhost:8001"

with sqlite3.connect("orders.db") as db:
    db.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            product TEXT NOT NULL
        )
    """)


@app.post("/orders")
async def create_order(user_id: int, product: str):

    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(f"{USER_SERVICE}/users/{user_id}")
            response.raise_for_status()

        user = response.json()

    except httpx.HTTPError:
        raise HTTPException(
            status_code=503, detail="Servicio de usuarios no disponible"
        )

    if "error" in user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    with sqlite3.connect("orders.db") as db:
        cursor = db.execute(
            """
            INSERT INTO orders (user_id, product)
            VALUES (?, ?)
            """,
            (user_id, product),
        )

        order_id = cursor.lastrowid

    return {"order_id": order_id, "user": user, "product": product}
