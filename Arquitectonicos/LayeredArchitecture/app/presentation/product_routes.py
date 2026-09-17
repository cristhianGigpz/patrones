class ProductController:
    def __init__(self, service):
        self.service = service

    def show_product(self, product_id):
        product = self.service.get_product(product_id)

        if product is None:
            print("Producto no encontrado")
            return

        print(product)
