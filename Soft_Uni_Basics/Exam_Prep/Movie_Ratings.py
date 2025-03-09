import sys

movies = int(input())
min_rating = sys.maxsize
max_rating = -sys.maxsize
total_rating = 0
highest_rating = ""
lowest_rating = ""

for i in range(movies):

    name = input()
    rating = float(input())

    total_rating += rating

    if rating < min_rating:
        min_rating = rating
        lowest_rating = name

    if rating > max_rating:
        max_rating = rating
        highest_rating = name

average = total_rating/movies
print(f"{highest_rating} is with highest rating: {max_rating}")
print(f"{lowest_rating} is with lowest rating: {min_rating}")
print(f"Average rating: {average:.1f}")
