name = input()
days = int(input())
tickets = int(input())
price = float(input())
percent = int(input())

tickets_for_day = tickets*price*days
for_cinema = tickets_for_day*percent/100
profit = tickets_for_day-for_cinema
print(f"The profit from the movie {name} is {profit:.2f} lv.")