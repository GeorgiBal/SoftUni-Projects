cars = int(input())
registered_cars = {}

for car in range(cars):
    command = input().split()

    if len(command) == 3:
        name = command[1]
        id_num = command[2]

        if name not in registered_cars.keys():
            registered_cars[name] = id_num
            print(f"{name} registered {id_num} successfully")
        else:
            print(f"ERROR: already registered with plate number {id_num}")

    else:
        name = command[1]

        if name not in registered_cars.keys():
            print(f"ERROR: user {name} not found")
        else:
            del registered_cars[name]
            print(f"{name} unregistered successfully")


for name, number in registered_cars.items():
    print(f"{name} => {number}")