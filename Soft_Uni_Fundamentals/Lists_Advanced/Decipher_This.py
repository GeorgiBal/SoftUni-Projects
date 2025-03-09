text = input().split()
new_text = []

for word in text:
    word = list(word)
    num = ''
    for i in word:
        if i.isdigit():
            num += i
    for i in num:
        word.remove(i)

    word.insert(0, chr(int(num)))
    word[1], word[-1] = word[-1], word[1]

    new_word = ''
    for i in word:
        new_word += i
    new_text.append(new_word)

print(*new_text)