lst1 = []
lst2_freq_dict = {}

with open("inputs/input1.txt", "r") as file:
    data = file.read()

for line in data.splitlines():
    temp = line.split("   ")
    lst1.append(int(temp[0]))
    lst2_freq_dict[int(temp[1])] = lst2_freq_dict.get(int(temp[1]), 0) + 1

total_similarity = 0

for element in lst1:
    total_similarity += element * lst2_freq_dict.get(element, 0)

print(total_similarity)

