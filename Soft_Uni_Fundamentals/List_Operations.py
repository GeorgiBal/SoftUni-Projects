# nums = list(range(1, 6))
# print(nums)
#
# text = "a, b, c"
# text_list = text.split(", ", 1)
# print(text_list)
#
# ls = ["a", "b", "c"]
# data = "-".join(ls)
# print(data)
#
# ints = [1, 2, 3, 4, 5]
# joined_numbers = ' '.join([str(n) for n in ints])
# print(joined_numbers)
#
# l = [1, 2, 3]
# l.append(2)
# l.remove(2)
# print(sum(l))
#
# my_list = [1, 2, 3, 4]
# my_list.sort(reverse=True)
# print(my_list)
#
# index = l.index(3)
# print(index)

n = int(input())
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_POSITIVE = "positive"
COMMAND_NEGATIVE = "negative"

numbers = [int(input()) for i in range(n)]

filtered_numbers = []

command = input()

for num in numbers:
    filtered_command = ((command == COMMAND_EVEN and num % 2 == 0) or
                        (command == COMMAND_ODD and num % 2 != 0) or
                        (command == COMMAND_POSITIVE and num >= 0) or
                        (command == COMMAND_EVEN and num <= 0)
                        )
    if filtered_command:
        filtered_numbers.append(num)

print(filtered_numbers)