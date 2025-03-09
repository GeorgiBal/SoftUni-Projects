budget = float(input())
video_card = int(input())
processor = int(input())
ram = int(input())

video_card_price = video_card * 250
processor_price = processor*(video_card_price*35/100)
ram_price = ram*(video_card_price*10/100)

total = video_card_price + processor_price + ram_price
if video_card > processor:
    total -= total*15/100

if budget >= total:
    print("You have {:.2f} leva left!".format(budget-total))
else:
    print("Not enough money! You need {:.2f} leva more!".format(total-budget))