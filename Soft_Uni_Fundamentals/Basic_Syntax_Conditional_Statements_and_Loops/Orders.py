n = int(input())
total_price = 0
for i in range(n):
    price = float(input())
    days = int(input())
    capsules = int(input())
    if not (0.01 <= price <= 100.00):
        continue
    elif not (1 <= days <= 31):
        continue
    elif not (1 <= capsules <= 2000):
        continue

    cost = price*days*capsules
    total_price += cost
    print(f"The price for the coffee is: ${cost:.2f}")


print(f"Total: ${total_price:.2f}")


