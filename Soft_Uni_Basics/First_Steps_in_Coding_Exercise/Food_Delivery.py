chicken = int(input())
fish = int(input())
vegan = int(input())

chicken_price = chicken*10.35
fish_price = fish*12.40
vegan_price = vegan*8.15

total_price = chicken_price + fish_price + vegan_price
dessert_price = total_price*20/100

final_sum = total_price + dessert_price + 2.50
print(round(final_sum, 2))