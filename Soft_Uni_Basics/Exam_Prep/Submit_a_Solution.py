budget = float(input())
products = 0
spending = 0
while True:
    name = input()

    if name == "Stop":
        print(f"You bought {products} products for {spending:.2f} leva.")
        break

    price = float(input())

    products += 1

    if products % 3 == 0:
        price /= 2

    if price > budget:
        print("You don't have enough money!")
        print(f"You need {price-budget:.2f} leva!")
        break

    spending += price
    budget -= price

