trainings = int(input())

shoes_price = trainings - (trainings*40/100)
suit_price = shoes_price - (shoes_price*20/100)
ball_price = suit_price/4
accessories_price = ball_price/5

final_sum = trainings + shoes_price + suit_price + ball_price + accessories_price
print(final_sum)