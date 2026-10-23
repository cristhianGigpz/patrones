from fastapi import FastAPI, HTTPException
import httpx
import random

app = FastAPI()

REGISTRY_URL = "http://localhost:8000"


@app.get("/checkout")
async def checkout():

    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(f"{REGISTRY_URL}/discover/payments")

            response.raise_for_status()

            instances = response.json()["instances"]

            payment_url = random.choice(instances)

            payment_response = await client.get(f"{payment_url}/pay")

            payment_response.raise_for_status()

            return payment_response.json()

    except httpx.HTTPError:
        raise HTTPException(status_code=503, detail="Servicio de pagos no disponible")
