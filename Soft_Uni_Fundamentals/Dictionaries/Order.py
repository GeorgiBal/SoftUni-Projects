products = {}

while True:
    product = input()

    if product == "buy":
        break

    name, price, quantity = product.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products.keys():
        products[name] = [price, quantity]
    else:
        products[name][0] = price
        products[name][1] += quantity

for key, value in products.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")
