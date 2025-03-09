electrons = int(input())
electrons_list = []
n = 1

while True:

    if electrons == 0:
        break

    shell = 2*(n**2)

    if electrons >= shell:
        electrons -= shell
        electrons_list.append(shell)
    else:
        electrons_list.append(electrons)
        break

    n += 1

print(electrons_list)