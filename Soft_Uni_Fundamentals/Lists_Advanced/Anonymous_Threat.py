def merge_text(text_list, start_index, end_index):

    if start_index < 0:
        start_index = 0

    if end_index >= len(text_list):
        end_index = len(text_list) - 1

    merged_string = ''.join(text_list[start_index:end_index + 1])
    text_list[start_index] = merged_string
    del text_list[start_index + 1:end_index + 1]


def divide_text(text_list, start_index, partitions):
    if start_index < 0:
        start_index = 0

    text = text_list[start_index]
    print(text/partitions)


words = input().split()

while True:
    command = input()
    if command == "3:1":
        break

    command = command.split()

    if command[0] == "merge":
        start = int(command[1])
        end = int(command[2])
        merge_text(words, start, end)
    elif command[0] == "divide":
        index = int(command[1])
        parts = int(command[2])
        divide_text(words, index, parts)


print(' '.join(words))






