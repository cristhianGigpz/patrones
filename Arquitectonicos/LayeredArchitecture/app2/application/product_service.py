class ProductService:
    def __init__(self, repository, domain):
        self.repository = repository
        self.domain = domain

    def get_product(self, product_id):
        product = self.repository.get_product(product_id)

        if product is None:
            return None

        return {**product, "price": self.domain.apply_discount(product["price"])}
