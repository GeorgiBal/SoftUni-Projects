days = 1
current_meters = 5364
while True:
    command = input()
    if command == "END":
        print("Failed!")
        print(f"{current_meters:.0f}")
        break
    elif command == "Yes":
        days += 1

    if days > 5:
        print("Failed!")
        print(f"{current_meters:.0f}")
        break

    meters = float(input())
    current_meters += meters
    if current_meters >= 8848:
        print(f"Goal reached for {days} days!")
        break

