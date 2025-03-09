book = input()
count = 0


while True:
    search = input()

    if search == book:
        print(f"You checked {count} books and found it.")
        break
    elif search == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {count} books.")
        break
    else:
        count += 1