flowers = input()
num = int(input())
budget = int(input())
price = 0

if flowers == "Roses":
    price = 5*num
    if num > 80:
        price -= price*10/100
elif flowers == "Dahlias":
    price = 3.8*num
    if num > 90:
        price -= price*15/100
elif flowers == "Tulips":
    price = 2.8*num
    if num > 80:
        price -= price*15/100
elif flowers == "Narcissus":
    price = 3*num
    if num < 120:
        price += price*15/100
elif flowers == "Gladiolus":
    price = 2.5*num
    if num < 80:
        price += price*20/100

if budget >= price:
    print(f"Hey, you have a great garden with {num} {flowers} and {budget-price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price-budget:.2f} leva more.")
