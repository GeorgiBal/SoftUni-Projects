nums = list(map(int, input().split(', ')))

positive = [num for num in nums if num >= 0]
negative = [num for num in nums if num < 0]
even = [num for num in nums if num % 2 == 0]
odd = [num for num in nums if num % 2 != 0]

positive = ', '.join(map(str, positive))
print(f'Positive: {positive}')
negative = ', '.join(map(str, negative))
print(f'Negative: {negative}')
even = ', '.join(map(str, even))
print(f'Even: {even}')
odd = ', '.join(map(str, odd))
print(f'Odd: {odd}')
