change = float(input())
coins = 0
change *= 100
change = int(change)
while True:
    if change - 200 >= 0:
        change -= 200
        coins += 1
    elif change - 100 >= 0:
        change -= 100
        coins += 1
    elif change - 50 >= 0:
        change -= 50
        coins += 1
    elif change - 20 >= 0:
        change -= 20
        coins += 1
    elif change - 10 >= 0:
        change -= 10
        coins += 1
    elif change - 5 >= 0:
        change -= 5
        coins += 1
    elif change - 2 >= 0:
        change -= 2
        coins += 1
    elif change - 1 >= 0:
        change -= 1
        coins += 1

    if change == 0:
        print(coins)
        break
