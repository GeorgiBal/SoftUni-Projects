town = input()
sales = float(input())
commission = 0

if town == "Sofia":
    if 0 <= sales <= 500:
        commission = 5/100
    elif 500 < sales <= 1000:
        commission = 7/100
    elif 1000 < sales <= 10000:
        commission = 8/100
    elif sales > 10000:
        commission = 12/100
    else:
        print("error")
elif town == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 5.5 / 100
    elif 500 < sales <= 1000:
        commission = 8 / 100
    elif 1000 < sales <= 10000:
        commission = 12 / 100
    elif sales > 10000:
        commission = 14.5 / 100
    else:
        print("error")
elif town == "Varna":
    if 0 <= sales <= 500:
        commission = 4.5 / 100
    elif 500 < sales <= 1000:
        commission = 7.5 / 100
    elif 1000 < sales <= 10000:
        commission = 10 / 100
    elif sales > 10000:
        commission = 13 / 100
    else:
        print("error")
else:
    print("error")

if commission != 0:
    print(f"{commission*sales:.2f}")