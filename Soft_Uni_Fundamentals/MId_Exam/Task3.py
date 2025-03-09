chat = []

while True:

    command = input().split()

    action = command[0]

    if action == "end":
        break

    message = command[1]

    if action == "Chat":
        chat.append(message)
    elif action == "Delete":
        if message in chat:
            chat.remove(message)
    elif action == "Edit":
        if message in chat:
            edited_message = command[2]
            index = chat.index(message)
            chat.insert(index, edited_message)
            chat.remove(message)
    elif action == "Pin":
        if message in chat:
            chat.remove(message)
            chat.append(message)
    elif action == "Spam":
        for i in range(1, len(command)):
            chat.append(command[i])


print(*chat, sep="\n")