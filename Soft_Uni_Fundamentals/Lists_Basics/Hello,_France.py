ticket = 150
items = input().split("|")
start_budget = float(input())
end_budget = start_budget
max_price = 0

bought_items = []

for item in items:
    item = item.split("->")
    type, price = item[0], float(item[1])

    if type == "Clothes":
        max_price = 50.00
    elif type == "Shoes":
        max_price = 35.00
    elif type == "Accessories":
        max_price = 20.50

    if price > max_price:
        continue
    elif price > end_budget:
        continue
    else:
        end_budget -= price
        item_price = price + (price*40/100)
        bought_items.append(item_price)

for product in bought_items:
    print(f"{product:.2f} ", end="")

print()
profit = (end_budget + sum(bought_items)) - start_budget
print(f"Profit: {profit:.2f}")

if end_budget + sum(bought_items) >= ticket:
    print("Hello, France!")
else:
    print("Not enough money.")





