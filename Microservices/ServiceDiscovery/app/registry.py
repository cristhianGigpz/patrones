from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

services = {}


class ServiceInstance(BaseModel):
    name: str
    url: str


@app.post("/register")
def register(instance: ServiceInstance):

    instances = services.setdefault(instance.name, [])

    if instance.url not in instances:
        instances.append(instance.url)

    return {"message": "Servicio registrado"}


@app.get("/discover/{name}")
def discover(name: str):

    instances = services.get(name, [])

    if not instances:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")

    return {"instances": instances}
