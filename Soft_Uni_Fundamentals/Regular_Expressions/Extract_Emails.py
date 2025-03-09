import re

string = input()
regex = r"\s(([a-z0-9]+[a-z0-9._-]*)@([a-z-]+)(\.[a-z]+)+)\b"

while string:
    matches = re.findall(regex, string)
    if matches:
        print(" ".join(matches), end=" ")
    string = input()
