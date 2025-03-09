def decrypting_message(message):
    while True:
        command = input()

        if command.startswith("End"):
            break
        elif command.startswith("Translate"):
            action, char, replacement = command.split()
            message = message.replace(char, replacement)
            print(message)
        elif command.startswith("Includes"):
            action, substring = command.split()
            if substring in message:
                print(True)
            else:
                print(False)
        elif command.startswith("Start"):
            action, substring = command.split()
            if message.startswith(substring):
                print(True)
            else:
                print(False)
        elif command.startswith("Lowercase"):
            message = message.lower()
            print(message)
        elif command.startswith("FindIndex"):
            action, char = command.split()
            print(message.rindex(char))
        elif command.startswith("Remove"):
            action, start_index, count = command.split()
            start_index = int(start_index)
            count = int(count)
            message = message[:start_index] + message[start_index + count:]
            print(message)


start_message = input()
decrypting_message(start_message)

