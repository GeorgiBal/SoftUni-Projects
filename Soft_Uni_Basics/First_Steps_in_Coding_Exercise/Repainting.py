nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_price = (nylon+2)*1.50
paint_price = (paint + (paint*10/100))*14.50
thinner_price = thinner*5
total = nylon_price + paint_price + thinner_price + 0.40

workers_price = (total*30/100)*hours
final_sum = total+workers_price
print(final_sum)