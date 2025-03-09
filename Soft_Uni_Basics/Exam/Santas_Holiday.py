days = int(input())
room = input()
rate = input()
price = 0

if room == "room for one person":
    price = (days-1)*18
elif room == "apartment":
    price = (days - 1) * 25
    if days < 10:
        price -= price*30/100
    elif 10 <= days <= 15:
        price -= price * 35 / 100
    elif days > 15:
        price -= price * 50 / 100
elif room == "president apartment":
    price = (days - 1) * 35
    if days < 10:
        price -= price * 10 / 100
    elif 10 <= days <= 15:
        price -= price * 15 / 100
    elif days > 15:
        price -= price * 20 / 100

if rate == "positive":
    price += price*25/100
elif rate == "negative":
    price -= price*10/100

print(f"{price:.2f}")
