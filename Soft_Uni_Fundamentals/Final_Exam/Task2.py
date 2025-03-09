import re

inputs = int(input())
regex = r"(\|)([A-Z]{4,})\1\:(\#)(([a-zA-Z]+) ([a-zA-Z]+))\3"

for i in range(inputs):
    names = input()
    matches = re.search(regex, names)
    if matches:
        print(f"{matches.group(2)}, The {matches.group(4)}\n>> Strength: {len(matches.group(2))}\n>> Armor: {len(matches.group(4))}")
    else:
        print("Access denied!")

