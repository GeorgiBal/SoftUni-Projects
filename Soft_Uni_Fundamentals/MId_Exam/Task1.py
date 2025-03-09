days = int(input())
players = int(input())
group_energy = float(input())
water_per_day = float(input())
food_per_day = float(input())

total_water = days * water_per_day * players
total_food = days * food_per_day * players

enough_energy = True

for day in range(1, days+1):
    energy_loss = float(input())
    group_energy -= energy_loss

    if group_energy <= 0:
        enough_energy = False
        break

    if day % 2 == 0:
        group_energy += group_energy * 5 / 100
        total_water -= total_water * 30 / 100

    if day % 3 == 0:
        total_food -= total_food / players
        group_energy += group_energy*10/100

if enough_energy:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")