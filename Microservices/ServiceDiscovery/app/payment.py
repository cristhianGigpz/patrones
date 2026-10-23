from fastapi import FastAPI

app = FastAPI()


@app.get("/pay")
def process_payment():
    return {"status": "success", "message": "Pago procesado"}
