month = input()
nights = int(input())
studio = 0
apartment = 0
discount = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if nights > 14:
        studio -= studio*30/100
    elif nights > 7:
        studio -= studio*5/100
elif month == "June" or month == "September":
    studio = 75.2
    apartment = 68.7
    if nights > 14:
        studio -= studio*20/100
elif month == "July" or month == "August":
    studio = 76
    apartment = 77

if nights > 14:
    apartment -= apartment*10/100


print(f"Apartment: {apartment*nights:.2f} lv.")
print(f"Studio: {studio*nights:.2f} lv.")

