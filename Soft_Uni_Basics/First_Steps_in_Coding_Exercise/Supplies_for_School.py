pens = int(input())
markers = int(input())
desk_cleaner = int(input())
percent_discount = int(input())

pens_price = pens*5.80
markers_price = markers*7.20
desk_cleaner_price = desk_cleaner*1.20

final_price = pens_price + markers_price + desk_cleaner_price
total = final_price - (final_price*percent_discount/100)
print(round(total, 2))