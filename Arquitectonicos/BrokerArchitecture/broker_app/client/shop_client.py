class ShopClient:
    def __init__(self, broker):
        self.broker = broker

    def buy(self, product_id):

        product = self.broker.request("products", "get_product", product_id)

        if product is None:
            return {"error": "Producto no encontrado"}

        payment = self.broker.request("payments", "process_payment", product["price"])

        return {"product": product, "payment": payment}
