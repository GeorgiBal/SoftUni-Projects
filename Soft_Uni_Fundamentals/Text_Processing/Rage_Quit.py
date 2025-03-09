text = input().upper()
message = ""
symbols = ""


for index in range(len(text)):

    if text[index].isdigit():

        digit = ""
        for num in range(index, len(text)):
            if not text[num].isdigit():
                break
            digit += text[num]

        message += int(digit)*symbols
        symbols = ""

    else:
        symbols += text[index]

print(f"Unique symbols used: {len(set(message))}")
print(message)


