nums = [int(num) for num in input().split()]
sum_removed = 0

while nums:
    index = int(input())

    if index < 0:
        index = 0
        nums.insert(index, nums[-1])
    elif index >= len(nums):
        index = -1
        nums.append(nums[0])

    removed = nums.pop(index)

    for i in range(len(nums)):
        if nums[i] <= removed:
            nums[i] += removed
        else:
            nums[i] -= removed

    sum_removed += removed

print(sum_removed)
