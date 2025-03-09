days = int(input())
total_wins = 0
total_loses = 0
total_money = 0
for i in range(days):
    money = 0
    wins = 0
    loses = 0
    while True:
        sport = input()
        if sport == "Finish":
            if wins > loses:
                money += money * 10 / 100

            total_wins += wins
            total_loses += loses
            total_money += money

            break
        result = input()
        if result == "win":
            money += 20
            wins += 1
        elif result == "lose":
            loses += 1


if total_wins > total_loses:
    total_money += total_money*20/100
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")

