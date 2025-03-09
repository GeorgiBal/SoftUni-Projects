age = int(input())
wm_price = float(input())
toy_price = int(input())

money = 0
toys = 0

for i in range(1, age+1):
    if i%2 == 0:
        money += ((i/2)*10)-1
    else:
        toys += 1

money += toy_price * toys
if money - wm_price >= 0:
    print(f"Yes! {money-wm_price:.2f}")
else:
    print(f"No! {abs(wm_price-money):.2f}")
    