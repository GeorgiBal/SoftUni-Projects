while True:
    money_have = 0
    destination = input()
    if destination == "End":
        break
    money_need = float(input())
    while money_have < money_need:
        money = float(input())
        money_have += money
    print(f"Going to {destination}!" )

