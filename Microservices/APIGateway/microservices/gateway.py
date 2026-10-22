from fastapi import FastAPI, HTTPException, Header
import httpx

app = FastAPI()

SERVICES = {
    "users": "http://localhost:8001",
    "products": "http://localhost:8002",
    "orders": "http://localhost:8003",
}


# GET http://localhost:8000/products
def validate_token(authorization: str = Header(default="")):
    if authorization != "Bearer demo-token":
        raise HTTPException(status_code=401, detail="No autorizado")


@app.get("/{service}")
async def gateway(service: str, authorization: str = Header(default="")):
    validate_token(authorization)

    if service not in SERVICES:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")

    url = f"{SERVICES[service]}/{service}"

    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(url)

        response.raise_for_status()
        return response.json()

    except httpx.HTTPError:
        raise HTTPException(
            status_code=502, detail="Error al consultar el microservicio"
        )


##uv run uvicorn gateway:app --port 8000
