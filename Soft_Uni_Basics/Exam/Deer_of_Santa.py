from math import ceil, floor

days = int(input())
food = int(input())
deer1 = float(input())
deer2 = float(input())
deer3 = float(input())

food1 = deer1 * days
food2 = deer2 * days
food3 = deer3 * days

total_food = food1 + food2 + food3
if total_food <= food:
    print(f"{floor(food - total_food)} kilos of food left.")
else:
    print(f"{ceil(total_food - food)} more kilos of food are needed.")
