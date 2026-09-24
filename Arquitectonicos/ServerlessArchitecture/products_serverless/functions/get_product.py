from services.product_service import find_product


def handler(event, context):

    product_id = int(event["pathParameters"]["id"])

    product = find_product(product_id)

    if product is None:
        return {"statusCode": 404, "body": "Producto no encontrado"}

    return {"statusCode": 200, "body": product}
