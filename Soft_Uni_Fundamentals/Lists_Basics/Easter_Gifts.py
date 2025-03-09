gifts = input().split()

while True:
    command = input()

    if command == "No Money":
        break

    command_parts = command.split()
    action = command_parts[0]
    gift = command_parts[1]

    if action == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = "None"

    elif action == "Required":
        index = int(command_parts[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif action == "JustInCase":
        gifts[-1] = gift

result = " ".join([g for g in gifts if g != "None"])
print(result)





