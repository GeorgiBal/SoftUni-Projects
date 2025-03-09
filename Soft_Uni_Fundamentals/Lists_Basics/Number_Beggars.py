numbers = input()
num_beggars = int(input())

numbers_list = [int(num) for num in numbers.split(", ")]
beggars = [0] * num_beggars

for i in range(len(numbers_list)):
    beggar_index = i % num_beggars
    beggars[beggar_index] += numbers_list[i]

print(beggars)



