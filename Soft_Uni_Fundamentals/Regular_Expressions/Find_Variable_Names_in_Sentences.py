import re

string = input()
regex = r"\b_([A-Za-z0-9]+)\b"

matches = re.findall(regex, string)
print(",".join(matches))

