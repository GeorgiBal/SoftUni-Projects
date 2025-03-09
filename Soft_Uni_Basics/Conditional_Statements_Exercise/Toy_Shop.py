trip = float(input())
puzzle = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzle_price = puzzle*2.60
dolls_price = dolls*3
bears_price = bears*4.10
minions_price = minions*8.20
trucks_price = trucks*2

order = puzzle_price + dolls_price + bears_price + minions_price + trucks_price
num_toys = puzzle + dolls + bears + minions + trucks

discount = 0
if num_toys >= 50:
    discount = order*25/100

final_sum = order - discount
rent = final_sum*10/100

profit = final_sum - rent

if profit >= trip:
    final = profit - trip
    print("Yes! {:.2f} lv left.".format(final))
else:
    final = trip - profit
    print("Not enough money! {:.2f} lv needed.".format(final))

