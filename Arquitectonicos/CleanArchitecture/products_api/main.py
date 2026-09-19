## uv init
## uv add fastapi uvicorn
## uv run uvicorn main:app --reload
from fastapi import FastAPI
from app.use_cases.get_product import GetProduct
from app.infraestructure.memory_repository import MemoryProductRepository
from app.adapters.product_controller import create_router


repository = MemoryProductRepository()

get_product = GetProduct(repository)

app = FastAPI()

app.include_router(create_router(get_product))
