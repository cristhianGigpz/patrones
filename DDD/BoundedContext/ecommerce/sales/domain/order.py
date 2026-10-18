from dataclasses import dataclass


@dataclass(frozen=True)
class OrderConfirmed:
    order_id: int
    product_id: int
    quantity: int
