from broker.broker import Broker

from services.product_service import ProductService
from services.payment_service import PaymentService

from client.shop_client import ShopClient


broker = Broker()

broker.register("products", ProductService())

broker.register("payments", PaymentService())

client = ShopClient(broker)

result = client.buy(1)

print(result)
