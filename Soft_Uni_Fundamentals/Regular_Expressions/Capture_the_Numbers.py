import re

string = input()
regex = r"\d+"

while string:
    matches = re.findall(regex, string)
    if matches:
        print(" ".join(matches), end=" ")
    string = input()



