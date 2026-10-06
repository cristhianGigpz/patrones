"""
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL
);

"""

import sqlite3


class Product:
    connection = sqlite3.connect("store.db")

    def __init__(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price

    def save(self):

        self.connection.execute(
            """
            INSERT OR REPLACE INTO products
            (id, name, price)
            VALUES (?, ?, ?)
            """,
            (self.id, self.name, self.price),
        )

        self.connection.commit()

    @classmethod
    def find(cls, product_id):

        cursor = cls.connection.execute(
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

        return cls(product_id=row[0], name=row[1], price=row[2])

    def apply_discount(self, percentage):

        if percentage < 0 or percentage > 100:
            raise ValueError("Descuento inválido")

        discount = self.price * percentage / 100

        self.price -= discount


# product = Product(5, "Tarjeta de vídeo", 3500)

# product.save()

# product = Product.find(5)

# print(product.name)
# print(product.price)

# product = Product.find(1)

# product.price = 1800

# product.save()

product = Product.find(1)

product.apply_discount(10)

product.save()
