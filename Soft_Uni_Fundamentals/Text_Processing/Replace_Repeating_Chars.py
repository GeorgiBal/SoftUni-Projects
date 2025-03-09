text = input()
final_text = ""
last_char = ""

for char in text:
    if char != last_char:
        last_char = char
        final_text += char

print(final_text)

