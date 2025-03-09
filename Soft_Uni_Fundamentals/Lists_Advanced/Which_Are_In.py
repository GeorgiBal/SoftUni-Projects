sequence1 = input().split(', ')
sequence2 = input().split(', ')
substrings = [substring for substring in sequence1 if any(substring in word for word in sequence2)]

# for substring in sequence1:
#     for word in sequence2:
#         if substring in word:
#             substrings.append(substring)
#             break


print(substrings)
