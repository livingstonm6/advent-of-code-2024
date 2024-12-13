with open("../inputs/input9.txt", "r") as file:
    data = file.read().rstrip("\n")

chars = []
id = 0
result = []

for i in range(0, len(data), 2):
    result += [id for _ in range(int(data[i]))]
    if i+1 < len(data):
        result += [None for _ in range(int(data[i+1]))]
    id += 1

l = 0
r = len(result) - 1

while l < r:
    while result[l] is not None:
        l += 1

    while result[r] is None:
        r -= 1

    if l >= r:
        break

    temp = result[l]
    result[l] = result[r]
    result[r] = temp

checksum = 0
i = 0
while result[i] is not None:
    checksum += result[i] * i
    i += 1

print(checksum)
