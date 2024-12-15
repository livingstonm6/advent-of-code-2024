with open("../inputs/input11.txt", "r") as file:
    data = file.read().strip()

stones = [int(x) for x in data.split(" ")]

cache = {}

def recur(stone, depth, max_depth):
    if depth == max_depth:
        return 1
    if (stone, depth) in cache:
        return cache[(stone, depth)]

    if stone == 0:
        val = recur(1, depth+1, max_depth)
    else:
        s = str(stone)
        if len(s) % 2 == 0:
            midpoint = len(s) // 2
            left = recur(int(s[:midpoint]), depth+1, max_depth)
            right = recur(int(s[midpoint:]), depth+1, max_depth)
            val = left + right
        else:
            val = recur(stone * 2024, depth+1, max_depth)

    cache[(stone, depth)] = val
    return val

i = 1
total = 0
for element in stones:
    print("Stone", i, "of", len(stones))
    total += recur(element, 0, 75)
    i += 1

print(total)