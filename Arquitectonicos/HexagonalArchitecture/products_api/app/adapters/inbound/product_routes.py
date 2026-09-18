from fastapi import APIRouter, HTTPException

from ...application.get_product import GetProduct


def create_router(get_product: GetProduct):

    router = APIRouter()

    @router.get("/products/{product_id}")
    def show_product(product_id: int):

        product = get_product.execute(product_id)

        if product is None:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

        return product

    return router
