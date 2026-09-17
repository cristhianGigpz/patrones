from application.product_service import ProductService
from domain.product import ProductDomain
from persistence.product_repository import ProductRepository
from presentation.product_routes import ProductController

repository = ProductRepository()
domain = ProductDomain()

service = ProductService(repository, domain)

controller = ProductController(service)

controller.show_product(5)
