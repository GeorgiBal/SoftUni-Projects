total = 0
while True:
    text = input()
    if text == "NoMoreMoney":
        break
    elif float(text) < 0:
        print("Invalid operation!")
        break
    else:
        total += float(text)
        print(f"Increase: {float(text):.2f}")

print(f"Total: {total:.2f}")