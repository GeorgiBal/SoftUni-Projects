budget = float(input())
nights = int(input())
price = float(input())
percent = int(input())

if nights > 7:
    price -= price*5/100

money = nights*price
expenses = budget*percent/100

total = money+expenses

if budget >= total:
    print(f"Ivanovi will be left with {budget-total:.2f} leva after vacation.")
else:
    print(f"{total-budget:.2f} leva needed.")