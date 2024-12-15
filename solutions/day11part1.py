from collections import deque

with open("../inputs/input11.txt", "r") as file:
    data = file.read().strip()

stones = deque([int(x) for x in data.split(" ")])

for blink in range(25):
    i = 0
    print("blink", blink + 1 , "of 25")
    length = len(stones)
    while i < length:
        stone = stones.popleft()
        if stone == 0:
            stones.append(1)
        else:
            s = str(stone)
            if len(s) % 2 == 0:
                midpoint = len(s) // 2
                stone1 = int(s[:midpoint])
                stone2 = int(s[midpoint:])
                stones.append(stone1)
                stones.append(stone2)
            else:
                stones.append(stone * 2024)

        i += 1

print(len(stones))