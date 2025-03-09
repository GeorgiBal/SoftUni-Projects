import re

places = input()
regex = r"(=|/)([A-Z]{1}[a-zA-Z]{2,})\1"
total_points = 0

matches = re.finditer(regex, places)
valid_destinations = []
for match in matches:
    total_points += len(match.group(2))
    valid_destinations.append(match.group(2))

print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {total_points}")

