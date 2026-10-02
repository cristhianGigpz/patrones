class Product:
    def __init__(self, product_id, name, price):
        if price <= 0:
            raise ValueError("Precio inválido")

        self.id = product_id
        self.name = name
        self.price = price
