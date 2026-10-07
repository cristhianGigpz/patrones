from dataclasses import dataclass


@dataclass
class Order:
    id: int
    customer: str
    total: float = 0.0
    status: str = "pending"


@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int


@dataclass
class Payment:
    id: int
    order_id: int
    amount: float
    status: str = "pending"


class Repository:
    def __init__(self):
        self._items = {}

    def insert(self, obj):
        key = (type(obj).__name__, obj.id)
        self._items[key] = obj
        return obj

    def update(self, obj):
        key = (type(obj).__name__, obj.id)
        if key not in self._items:
            raise KeyError(f"El objeto {obj} no existe en el repositorio.")
        self._items[key] = obj
        return obj

    def delete(self, obj):
        key = (type(obj).__name__, obj.id)
        self._items.pop(key, None)

    def get_all(self):
        return list(self._items.values())


class UnitOfWork:
    def __init__(self, repository):
        self.repository = repository

        self.new = []
        self.modified = []
        self.deleted = []

    def register_new(self, obj):
        self.new.append(obj)

    def register_modified(self, obj):
        self.modified.append(obj)

    def register_deleted(self, obj):
        self.deleted.append(obj)

    def commit(self):
        for obj in self.new:
            self.repository.insert(obj)

        for obj in self.modified:
            self.repository.update(obj)

        for obj in self.deleted:
            self.repository.delete(obj)

        self.clear()

    def clear(self):
        self.new.clear()
        self.modified.clear()
        self.deleted.clear()


repository = Repository()
uow = UnitOfWork(repository)

order = Order(id=1, customer="Ana", total=250.0)
product = Product(id=10, name="Teclado mecánico", price=120.0, stock=5)
payment = Payment(id=1, order_id=1, amount=250.0)

repository.insert(product)
product.stock -= 1


uow.register_new(order)
uow.register_modified(product)
uow.register_new(payment)

uow.commit()

print("Objetos guardados:")
for obj in repository.get_all():
    print(obj)
