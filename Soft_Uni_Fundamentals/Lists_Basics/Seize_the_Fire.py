fire_cells = input().split("#")
water = int(input())
total_fire = 0
total_effort = 0
valid_cells = []
high = range(81, 125+1)
medium = range(51, 80+1)
low = range(1, 50+1)


for cell in fire_cells:
    type_of_fire, cell_value = cell.split(" = ")
    cell_value = int(cell_value)
    is_valid = False
    if type_of_fire == "High":
        if cell_value in high:
            is_valid = True
    elif type_of_fire == "Medium":
        if cell_value in medium:
            is_valid = True
    elif type_of_fire == "Low":
        if cell_value in low:
            is_valid = True

    if is_valid:
        if water >= cell_value:
            water -= cell_value
            valid_cells.append(cell_value)
            total_fire += cell_value
            total_effort += cell_value*0.25


print("Cells: ")
for cell in valid_cells:
    print(f"- {cell}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
