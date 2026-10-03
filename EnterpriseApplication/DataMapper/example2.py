import sqlite3


class Product:
    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price

    def apply_discount(self, percentage):
        self.price -= self.price * percentage / 100


class ProductRepository:
    def __init__(self, mapper):
        self.mapper = mapper

    def find_by_id(self, product_id):
        return self.mapper.find_by_id(product_id)

    def save(self, product):
        self.mapper.insert(product)


class ProductMapper:
    def __init__(self, connection):
        self.connection = connection

    def find_by_id(self, product_id):

        cursor = self.connection.execute(
            """
            SELECT id, name, price
            FROM products
            WHERE id = ?
            """,
            (product_id,),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Product(product_id=row[0], name=row[1], price=row[2])

    def insert(self, product):

        self.connection.execute(
            """
            INSERT INTO products
            (id, name, price)
            VALUES (?, ?, ?)
            """,
            (product.id, product.name, product.price),
        )

        self.connection.commit()


connection = sqlite3.connect("store.db")
connection.execute(
    """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
    """
)

mapper = ProductMapper(connection)
repository = ProductRepository(mapper)

product = Product(4, "Pc", 2200)

repository.save(product)


product = repository.find_by_id(4)

print(product.name)
