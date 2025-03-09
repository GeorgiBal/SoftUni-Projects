import re

string = input()
regex = r"(w{3}\.[A-Za-z0-9-\.]+\.[a-z]+)"

while string:
    matches = re.findall(regex, string)
    if matches:
        print("\n".join(matches))
    string = input()