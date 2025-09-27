#MARKET_PY

products_list = []

products = {
    "product": input("Product: "),
    "brand": input("Brand: "),
    "price": float(input("Price: ")),
    "expiration": input("Expiration date: ")
}


products_list.append(products)
print(products_list)
print(products["brand"])