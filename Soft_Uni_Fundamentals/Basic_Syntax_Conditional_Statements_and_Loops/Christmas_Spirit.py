quantity = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

budget = 0
totalSpirit = 0

for i in range(1, days+1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        budget += quantity * ornament_set
        totalSpirit += 5
    if i % 3 == 0:
        budget += quantity * (tree_skirt + tree_garland)
        totalSpirit += 13
    if i % 5 == 0:
        budget += quantity * tree_lights
        totalSpirit += 17
        if i % 3 == 0:
            totalSpirit += 30
    if i % 10 == 0:
        budget += tree_skirt + tree_garland + tree_lights
        totalSpirit -= 20


if days % 10 == 0:
    totalSpirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {totalSpirit}")

