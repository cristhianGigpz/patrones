class InventoryHandler:
    def __init__(self, repository):
        self.repository = repository

    def handle(self, event):

        product = self.repository.find_by_id(event.product_id)

        if product is None:
            raise ValueError("Producto no encontrado")

        product.remove_stock(event.quantity)

        self.repository.save(product)
