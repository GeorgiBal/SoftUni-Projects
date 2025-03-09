film = float(input())
statists = int(input())
clothing = float(input())

decor_price = film*10/100
clothing_price = statists*clothing

if statists > 150:
    clothing_price -= clothing_price*10/100

total_sum = decor_price + clothing_price

if film >= total_sum:
    print("Action!")
    print("Wingard starts filming with {:.2f} leva left.".format(film-total_sum))
else:
    print("Not enough money!")
    print("Wingard needs {:.2f} leva more.".format(total_sum - film))
