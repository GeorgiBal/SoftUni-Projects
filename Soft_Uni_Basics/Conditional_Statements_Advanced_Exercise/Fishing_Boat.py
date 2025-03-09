budget = int(input())
season = input()
people = int(input())
price = 0
discount = 0

if people <= 6:
    discount = 10 / 100
elif 7 <= people <= 11:
    discount = 15 / 100
elif people > 12:
    discount = 25 / 100

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

total = price - (price*discount)

if people%2 == 0 and season != "Autumn":
    total -= total*5/100

if budget >= total:
    print(f"Yes! You have {budget-total:.2f} leva left.")
else:
    print(f"Not enough money! You need {total-budget:.2f} leva.")
