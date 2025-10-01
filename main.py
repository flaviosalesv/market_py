#MARKET_PY

products_list = []

while len(products_list) < 3:
    products = {
    "product": input("Product: "),
    "brand": input("Brand: "),
    "price": float(input("Price: ")),
    "expiration": input("Expiration date: ")
}

    products_list.append(products)

    if len(products_list) < 3:
        add_more = input("Do you want to add another product? (y/n): ")
        if add_more != 'y':
            break

#print(products_list)
#print(products["brand"])