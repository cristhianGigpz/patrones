from fastapi import FastAPI

from controllers.product_controller import create_router

from services.product_service import ProductService

from repositories.product_repository import ProductRepository


app = FastAPI()

repository = ProductRepository()

service = ProductService(repository)

router = create_router(service)

app.include_router(router)

## uv init
## uv add fastapi uvicorn
## uv run uvicorn main:app --reload
