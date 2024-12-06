lst1 = []
lst2 = []

with open("../inputs/input1.txt", "r") as file:
    data = file.read()

for line in data.splitlines():
    temp = line.split("   ")
    lst1.append(int(temp[0]))
    lst2.append(int(temp[1]))

lst1.sort()
lst2.sort()

total_dist = 0

for i in range(len(lst1)):
    total_dist += abs(lst1[i] - lst2[i])

print(total_dist)

