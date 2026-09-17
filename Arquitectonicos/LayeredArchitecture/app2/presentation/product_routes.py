# class ProductController:
#     def __init__(self, service):
#         self.service = service

#     def show_product(self, product_id):
#         product = self.service.get_product(product_id)

#         if product is None:
#             print("Producto no encontrado")
#             return

#         print(product)
from fastapi import APIRouter, HTTPException
from application.product_service import ProductService
from domain.product import ProductDomain
from persistence.product_repository import ProductRepository

router = APIRouter()

repository = ProductRepository()
domain = ProductDomain()

service = ProductService(repository, domain)


@router.get("/products/{product_id}")
def get_product(product_id: int):

    product = service.get_product(product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return product
