text = [char for char in input() if char != " "]
chars = {}

for letter in text:
    if letter in chars.keys():
        chars[letter] += 1
    else:
        chars[letter] = 1

for key, value in chars.items():
    print(f"{key} -> {value}")