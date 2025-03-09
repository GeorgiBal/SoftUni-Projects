budget = float(input())
season = input()
destination = ""
discount = 0
price = 0
place = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        discount = 30/100
        place = "Camp"
    elif season == "winter":
        discount = 70/100
        place = "Hotel"
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        discount = 40/100
        place = "Camp"
    elif season == "winter":
        discount = 80/100
        place = "Hotel"
elif budget > 1000:
    destination = "Europe"
    discount = 90/100
    place = "Hotel"

price = discount*budget
print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")

