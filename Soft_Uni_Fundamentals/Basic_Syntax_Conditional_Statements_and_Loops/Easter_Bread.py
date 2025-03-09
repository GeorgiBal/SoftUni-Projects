budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 75 / 100
milk_price = flour_price + flour_price * 25 / 100
milk_price = milk_price / 4

loaves = 0
colored_eggs = 0

while True:
    if budget - (flour_price + eggs_price + milk_price) <= 0:
        break
    else:
        budget -= flour_price + eggs_price + milk_price
        loaves += 1
        colored_eggs += 3
        if loaves % 3 == 0:
            colored_eggs -= loaves - 2

print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
