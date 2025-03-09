is_even = lambda x: int(x) % 2 == 0

numbers = input()
numbers_list = [int(num) for num in numbers.split(" ")]
filtered_numbers = list(filter(is_even, numbers_list))
print(filtered_numbers)
