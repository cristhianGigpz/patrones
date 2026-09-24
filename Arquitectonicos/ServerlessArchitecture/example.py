def calculate_price(event):

    price = event["price"]

    final_price = price * 0.90

    return {"price": final_price}


event = {"price": 2000}

result = calculate_price(event)

print(result)
