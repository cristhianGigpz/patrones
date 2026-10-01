from fastapi import APIRouter, HTTPException

router = APIRouter()


def create_router(service):

    @router.post("/products")
    def create_product(data: dict):

        try:
            product = service.create_product(data["id"], data["name"], data["price"])

            return {"id": product.id, "name": product.name, "price": product.price}

        except ValueError as error:
            raise HTTPException(status_code=400, detail=str(error))

    @router.get("/products/{product_id}")
    def get_product(product_id: int):

        try:
            product = service.get_product(product_id)

            return {"id": product.id, "name": product.name, "price": product.price}

        except ValueError as error:
            raise HTTPException(status_code=404, detail=str(error))

    return router
