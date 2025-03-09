paper = int(input())
cloth = int(input())
glue = float(input())
discount = int(input())

paper_price = paper*5.8
cloth_price = cloth*7.2
glue_price = glue*1.2
price = paper_price + cloth_price + glue_price
price -= price*discount/100
print(f"{price:.3f}")
