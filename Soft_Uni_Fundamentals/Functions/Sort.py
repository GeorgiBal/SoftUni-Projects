def sort_nums(nums):
    return sorted(nums)


numbers = input()
numbers_list = [int(num) for num in numbers.split(" ")]
print(sort_nums(numbers_list))