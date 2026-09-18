from .ports import ProductRepository


class GetProduct:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: int):
        product = self.repository.get_product(product_id)

        if product is None:
            return None

        return {"name": product.name, "price": product.discounted_price()}
