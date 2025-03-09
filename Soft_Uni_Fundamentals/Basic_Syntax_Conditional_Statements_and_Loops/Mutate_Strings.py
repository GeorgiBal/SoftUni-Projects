text1 = input()
text2 = input()

text1 = list(text1)
text2 = list(text2)

for i in range(len(text1)):
    if text1[i] != text2[i]:
        text1[i] = text2[i]
        print("".join(text1))

