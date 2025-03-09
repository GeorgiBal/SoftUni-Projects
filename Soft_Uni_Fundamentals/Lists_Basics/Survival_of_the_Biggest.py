numbers = input()
numbers_list = [int(num) for num in numbers.split()]
n = int(input())

remaining_nums = sorted(numbers_list)[n:]

final_nums = []

for i in numbers_list:
    if i in remaining_nums:
        final_nums.append(i)

result = ", ".join(str(num) for num in final_nums)
print(result)

