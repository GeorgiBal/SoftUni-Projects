deposit = float(input())
months = int(input())
percent = float(input())

interest = deposit*percent/100
month_interest = interest/12

total = deposit + (months*month_interest)
print(total)