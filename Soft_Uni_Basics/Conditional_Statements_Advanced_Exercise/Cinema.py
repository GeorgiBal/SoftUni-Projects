movie = input()
rows = int(input())
columns = int(input())
price = 0

if movie == "Premiere":
    price = 12
elif movie == "Normal":
    price = 7.5
elif movie == "Discount":
    price = 5

print(f"{price*rows*columns:.2f} leva")
