routes = input().split("||")
fuel = int(input())
ammunition = int(input())

for rout in routes:

    rout_parts = rout.split()
    command = rout_parts[0]

    if command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    else:
        number = int(rout_parts[1])

    if command == "Travel":
        if fuel >= number:
            fuel -= number
            print(f"The spaceship travelled {number} light-years.")
        else:
            print("Mission failed.")
            break
    elif command == "Enemy":
        if ammunition >= number:
            ammunition -= number
            print(f"An enemy with {number} armour is defeated.")
        elif fuel - number*2 >= 0:
            fuel -= number*2
            print(f"An enemy with {number} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break
    elif command == "Repair":
        added_fuel = number
        added_ammunitions = number*2

        fuel += added_fuel
        ammunition += added_ammunitions

        print(f"Ammunitions added: {added_ammunitions}.")
        print(f"Fuel added: {added_fuel}.")



