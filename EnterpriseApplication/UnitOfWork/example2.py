import sqlite3


class UnitOfWork:
    def __init__(self, connection):
        self.connection = connection

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()


class OrderRepository:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, order):
        cursor = self.connection.execute(
            """
                    INSERT INTO orders (product_id, quantity)
                    VALUES (?, ?)
                    """,
            (order["product_id"], order["quantity"]),
        )
        order["id"] = cursor.lastrowid
        return order


class ProductRepository:
    def __init__(self, connection):
        self.connection = connection

    def find_by_id(self, product_id):
        cursor = self.connection.execute(
            """
            SELECT id, name, price, stock
            FROM products
            WHERE id = ?
            """,
            (product_id,),
        )
        row = cursor.fetchone()
        if row is None:
            return None
        return {"id": row[0], "name": row[1], "price": row[2], "stock": row[3]}

    def update(self, product):
        self.connection.execute(
            """
            UPDATE products
            SET name = ?, price = ?, stock = ?
            WHERE id = ?
            """,
            (product["name"], product["price"], product["stock"], product["id"]),
        )


class OrderService:
    def __init__(self, order_repository, product_repository, unit_of_work):
        self.orders = order_repository
        self.products = product_repository
        self.uow = unit_of_work

    def create_order(self, product_id, quantity):
        try:
            if (
                not isinstance(quantity, int)
                or isinstance(quantity, bool)
                or quantity <= 0
            ):
                raise ValueError("La cantidad debe ser un entero positivo")

            product = self.products.find_by_id(product_id)

            if product is None:
                raise ValueError("Producto no encontrado")

            if product["stock"] < quantity:
                raise ValueError("Stock insuficiente")

            product["stock"] -= quantity

            order = {"product_id": product_id, "quantity": quantity}

            self.products.update(product)
            self.orders.insert(order)

            self.uow.commit()

            return order

        except Exception:
            self.uow.rollback()
            raise


def main():
    # Ambos repositorios comparten la conexión y, por tanto, la transacción.
    connection = sqlite3.connect("store.db")
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL CHECK (price >= 0),
                stock INTEGER NOT NULL CHECK (stock >= 0)
            );

            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                product_id INTEGER NOT NULL REFERENCES products(id),
                quantity INTEGER NOT NULL CHECK (quantity > 0)
            );
            """
        )

        connection.execute(
            """
            INSERT INTO products (id, name, price, stock) VALUES (?, ?, ?, ?)
            ON CONFLICT(id) DO NOTHING
            """,
            (7, "Mouse inalámbrico", 50.0, 5),
        )
        connection.commit()

        orders = OrderRepository(connection)
        products = ProductRepository(connection)
        uow = UnitOfWork(connection)
        service = OrderService(orders, products, uow)

        try:
            order = service.create_order(product_id=7, quantity=2)
            print("Orden confirmada:", order)
        except ValueError as error:
            print("Compra rechazada:", error)
        print("Stock después de la compra:", products.find_by_id(7)["stock"])

    finally:
        connection.close()


if __name__ == "__main__":
    main()
