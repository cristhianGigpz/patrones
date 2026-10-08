class Product:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price


class IdentityMap:
    def __init__(self):
        self.objects = {}

    def get(self, object_id):
        return self.objects.get(object_id)

    def add(self, obj):
        self.objects[obj.id] = obj

    def clear(self):
        self.objects.clear()


identity_map = IdentityMap()

product = Product(1, "Laptop", 2000)

identity_map.add(product)

product1 = identity_map.get(1)
product2 = identity_map.get(1)

print(product1 is product2)

product1.price = 1800

print(product2.price)
