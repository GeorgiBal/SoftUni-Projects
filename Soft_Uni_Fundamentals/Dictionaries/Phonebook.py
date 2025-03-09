notebook = {}

while True:
    contact = input()
    if contact.isdigit():
        digit = int(contact)
        break

    name, number = contact.split("-")
    notebook[name] = number

for i in range(digit):
    name = input()
    if name in notebook.keys():
        print(f"{name} -> {notebook[name]}")
    else:
        print(f"Contact {name} does not exist.")