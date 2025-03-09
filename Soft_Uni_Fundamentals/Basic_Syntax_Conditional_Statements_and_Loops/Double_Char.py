
while True:
    text = input()
    if text == "End":
        break

    if text == "SoftUni":
        continue
    new_text = ""
    for i in text:
        new_text += i*2
    print(new_text)
