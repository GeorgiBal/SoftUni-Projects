version = list(map(int, input().split('.')))
version.reverse()
for index in range(len(version)):
    if version[index] == 9:
        version[index] = 0
    else:
        version[index] += 1
        break

version.reverse()
version = '.'.join(map(str, version))
print(version)