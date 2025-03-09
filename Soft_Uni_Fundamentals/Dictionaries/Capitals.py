countries = input().split(", ")
capitals = input().split(", ")

# information = {countries[index]: capitals[index] for index in range(len(countries))}
nations = dict(zip(countries, capitals))

for key, value in nations.items():
    print(f"{key} -> {value}")
