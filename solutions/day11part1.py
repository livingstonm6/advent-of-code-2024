with open("../inputs/input11.txt", "r") as file:
    data = file.read().strip()

stones = [int(x) for x in data.split(" ")]

for blink in range(25):
    i = 0
    print("blink", blink + 1 , "of 25")
    while i < len(stones):
        if stones[i] == 0:
            stones[i] = 1
            i += 1
        elif len(str(stones[i])) % 2 == 0:
            midpoint = len(str(stones[i])) // 2
            stone1 = int(str(stones[i])[:midpoint])
            stone2 = int(str(stones[i])[midpoint:])
            stones = stones[:i] + [stone1, stone2] + stones[i+1:]
            i += 2
        else:
            stones[i] = stones[i] * 2024
            i += 1

print(len(stones))