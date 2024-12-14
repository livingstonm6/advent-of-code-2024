with open("../inputs/input9.txt", "r") as file:
    data = file.read().rstrip("\n")

id = 0
result = []

for i in range(0, len(data), 2):
    result += [id for _ in range(int(data[i]))]
    if i+1 < len(data):
        result += [None for _ in range(int(data[i+1]))]
    id += 1

start_l = result.index(None)
r = len(result) - 1

while start_l < r:
    while result[r] is None:
        r -= 1

    r_l = r
    while result[r] == result[r_l]:
        r_l -= 1

    l = start_l
    l_r = start_l + (r - r_l)

    while l_r <= r_l + 1 and set(result[l:l_r]) != {None}:
        l += 1
        l_r += 1

    if l_r > r_l + 1:
        r = r_l
        continue

    for i in range(r, r_l, -1):
        j = l + (r - i)

        temp = result[i]
        result[i] = result[j]
        result[j] = temp

    start_l = result.index(None)
    r = r_l

checksum = 0
for i in range(len(result)):
    if result[i] is not None:
        checksum += result[i] * i

print(checksum)
