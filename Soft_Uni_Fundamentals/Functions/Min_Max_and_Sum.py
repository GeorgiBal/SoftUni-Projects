def min_max_and_sum(nums):
    print(f"The minimum number is {min(nums)}")
    print(f"The maximum number is {max(nums)}")
    print(f"The sum number is: {sum(nums)}")


numbers = input()
numbers_list = [int(num) for num in numbers.split(" ")]
min_max_and_sum(numbers_list)