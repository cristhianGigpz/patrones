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

    # def get(self, entity_type, object_id):
    #     key = (entity_type, object_id)
    #     return self.objects.get(key)

    def add(self, obj):
        self.objects[obj.id] = obj

    def clear(self):
        self.objects.clear()


class ProductRepository:
    def __init__(self, database, identity_map):
        self.database = database
        self.identity_map = identity_map

    def find_by_id(self, product_id):

        # Primero buscar en memoria
        product = self.identity_map.get(product_id)

        if product is not None:
            return product

        # Si no existe, consultar la DB
        row = self.database.get(product_id)

        if row is None:
            return None

        product = Product(product_id, row["name"], row["price"])

        # Registrar el objeto
        self.identity_map.add(product)

        return product


database = {
    1: {"name": "Laptop", "price": 2000},
    2: {"name": "Smartphone", "price": 800},
    3: {"name": "Tablet", "price": 500},
}

identity_map = IdentityMap()

repository = ProductRepository(database, identity_map)

product1 = repository.find_by_id(1)
product2 = repository.find_by_id(1)

print(product1 is product2)
