from fastapi import FastAPI
from presentation.product_routes import router

app = FastAPI()

app.include_router(router)

## uv init
## uv add fastapi uvicorn
## uv run uvicorn main:app --reload
