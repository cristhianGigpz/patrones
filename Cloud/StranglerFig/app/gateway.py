from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

LEGACY_URL = "http://127.0.0.1:8001"
NEW_URL = "http://127.0.0.1:8002"

MIGRATED_ROUTES = {"/products"}


@app.get("/{path:path}")
async def gateway(path: str):
    route = f"/{path}"

    # base_url = NEW_URL if route in MIGRATED_ROUTES else LEGACY_URL

    # async with httpx.AsyncClient(timeout=5) as client:
    #     try:
    #         response = await client.get(base_url + route)
    #         return response.json()

    #     except (httpx.RequestError, ValueError):
    #         raise HTTPException(status_code=502, detail="Error del servicio de destino")
    async with httpx.AsyncClient(timeout=5) as client:
        # 1. Si la ruta está migrada, intentamos llamar al servicio NUEVO
        if route in MIGRATED_ROUTES:
            try:
                response = await client.get(NEW_URL + route)
                return response.json()
            except (httpx.RequestError, ValueError):
                # Si falla el nuevo, no lanzamos error; dejamos que el código continúe al LEGACY
                pass

        # 2. Si la ruta no estaba migrada, O si el servicio nuevo falló, usamos el LEGACY
        try:
            response = await client.get(LEGACY_URL + route)
            return response.json()
        except (httpx.RequestError, ValueError):
            raise HTTPException(
                status_code=502, detail="Ambos servicios (Nuevo y Legacy) están caídos"
            )
