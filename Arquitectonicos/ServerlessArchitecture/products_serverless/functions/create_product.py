from services.product_service import save_product


def handler(event, context):

    product = event["body"]

    created_product = save_product(product)

    return {"statusCode": 201, "body": created_product}
