import re

total_price = 0
regex = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
names = []

while True:
    bought_furniture = input()

    if bought_furniture == "Purchase":
        break

    match = re.search(regex, bought_furniture)

    if match:
        furniture, price, quantity = match.groups()
        total_price += float(price)*int(quantity)
        names.append(furniture)

print("Bought furniture:")
for name in names:
    print(name)
print(f"Total money spend: {total_price:.2f}")
