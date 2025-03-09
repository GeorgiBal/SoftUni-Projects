collection = {}

while True:
    resource = input()
    if resource == "stop":
        break

    quantity = int(input())

    if resource in collection.keys():
        collection[resource] += quantity
    else:
        collection[resource] = quantity

for key, value in collection.items():
    print(f"{key} -> {value}")