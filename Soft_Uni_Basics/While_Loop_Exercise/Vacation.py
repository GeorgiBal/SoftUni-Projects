money_need = float(input())
money_have = float(input())
spend_days = 0
days = 0

while True:
    command = input()
    money = float(input())
    days += 1

    if command == "spend":
        spend_days += 1
        money_have -= money
        if money_have < 0:
            money_have = 0
    elif command == "save":
        spend_days = 0
        money_have += money

    if money_have >= money_need:
        print(f"You saved the money for {days} days.")
        break
    elif spend_days == 5:
        print("You can't save the money.")
        print(f"{days}")
        break


