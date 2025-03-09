student = 0
standard = 0
kid = 0
tickets = 0

while True:
    movie = input()
    count = 0

    if movie == "Finish":
        print(f"Total tickets: {tickets}")
        print(f"{student*100/tickets:.2f}% student tickets.")
        print(f"{standard*100/tickets:.2f}% standard tickets.")
        print(f"{kid*100/tickets:.2f}% kids tickets.")
        break
    seats = int(input())
    for i in range(seats):
        ticket = input()
        if ticket == "End":
            break
        elif ticket == "student":
            student += 1
            count += 1
        elif ticket == "standard":
            standard += 1
            count += 1
        elif ticket == "kid":
            kid += 1
            count += 1

    tickets += count
    print(f"{movie} - {count*100/seats:.2f}% full.")
