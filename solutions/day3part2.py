with open("../inputs/input3.txt", "r") as file:
    data = file.read()

valid_chars = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ","}
result = 0
i = 0
enabled = True

while i < len(data):
    j = i + 4

    while data[i:j] != "mul(" and j < len(data):
        if data[i:j] == "do()":
            enabled = True
        elif j + 3 < len(data) and data[i:j+3] == "don't()":
            enabled = False
        i += 1
        j += 1

    if j == len(data):
        break

    i = j
    valid = True
    while j < len(data) and data[j] != ")":
        if data[j] not in valid_chars:
            valid = False
            break
        j += 1

    if j == len(data):
        break

    if valid and enabled:
        nums = data[i:j].split(",")
        if len(nums) == 2:
            result += (int(nums[0]) * int(nums[1]))

    i = j

print(result)