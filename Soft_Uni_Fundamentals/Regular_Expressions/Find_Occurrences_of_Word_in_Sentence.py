import re

string = input()
word = input()
regex = fr"\b{word}\b"
matches = re.findall(regex, string, flags=re.IGNORECASE)
print(len(matches))
