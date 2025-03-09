def odd_and_even_sum(nums):
    odd = 0
    even = 0
    for i in nums:
        if int(i) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)

    return f"Odd sum = {odd}, Even sum = {even}"


numbers = input()
print(odd_and_even_sum(numbers))

