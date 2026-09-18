from fastapi import FastAPI
from app.adapters.inbound.product_routes import create_router
from app.adapters.outbound.memory_repository import MemoryProductRepository
from app.application.get_product import GetProduct


repository = MemoryProductRepository()

get_product = GetProduct(repository)

app = FastAPI()

app.include_router(create_router(get_product))

## uv init
## uv add fastapi uvicorn
## uv run uvicorn main:app --reload
