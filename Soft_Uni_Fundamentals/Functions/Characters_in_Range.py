def char_in_range(ch1, ch2):
    chars = []
    for i in range(ord(ch1) + 1, ord(ch2)):
        chars.append(chr(i))
    return chars


char1 = input()
char2 = input()

print(*char_in_range(char1, char2))