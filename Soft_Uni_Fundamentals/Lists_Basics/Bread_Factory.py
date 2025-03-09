energy = 100
coins = 100
events = input().split("|")

day_completed = True

for event in events:
    command, number = event.split("-")

    if command == "rest":
        cur_energy = energy
        energy += number
        if energy > 100:
            energy = 100
        gained_energy = energy - cur_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif command == "order":
        if energy - 30 >= 0:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {command}.")
        else:
            print(f"Closed! Cannot afford {command}.")
            day_completed = False
            break

if day_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")


