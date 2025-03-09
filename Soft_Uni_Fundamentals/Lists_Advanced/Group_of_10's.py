nums = list(map(int, input().split(', ')))
current_group = 10

while nums:
    filtered_group = [num for num in nums if num <= current_group]
    # for num in nums:
    #     if num <= current_group:
    #         current_numbers.append(num)

    print(f"Group of {current_group}'s:", filtered_group)
    current_group += 10
    nums = [num for num in nums if num not in filtered_group]
