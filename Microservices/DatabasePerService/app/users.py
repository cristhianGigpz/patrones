import sqlite3
from fastapi import FastAPI

app = FastAPI()

with sqlite3.connect("users.db") as db:
    db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)
    # db.execute("INSERT OR IGNORE INTO users VALUES (?, ?)", (1, "Ana"))
##Para probar el sistema, insertamos previamente un usuario en users.db:


@app.get("/users/{user_id}")
def get_user(user_id: int):

    with sqlite3.connect("users.db") as db:
        user = db.execute(
            "SELECT id, name FROM users WHERE id = ?", (user_id,)
        ).fetchone()

    if not user:
        return {"error": "Usuario no encontrado"}

    return {"id": user[0], "name": user[1]}
