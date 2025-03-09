days = int(input())
hours = int(input())
total = 0

for day in range(1, days+1):
    price = 0
    for hour in range(1, hours+1):
        if day % 2 == 0 and hour % 2 != 0:
            price += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            price += 1.25
        else:
            price += 1

    total += price
    print(f"Day: {day} - {price:.2f} leva")

print(f"Total: {total:.2f} leva")
