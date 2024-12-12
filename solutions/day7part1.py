from collections import deque

with open("../inputs/input7.txt", "r") as file:
    data = file.read()

total = 0

for line in data.splitlines():
    temp = line.split(": ")
    target = int(temp[0])
    nums = deque([int(x) for x in temp[1].split(" ")])
    valid = [False]

    def recur():
        if len(nums) == 1:
            if nums[0] == target:
                valid[0] = True
            return

        operand1 = nums.popleft()
        operand2 = nums.popleft()

        nums.appendleft(operand1 + operand2)
        recur()
        nums.popleft()

        nums.appendleft(operand1 * operand2)
        recur()
        nums.popleft()

        nums.appendleft(operand2)
        nums.appendleft(operand1)

    recur()

    if valid[0]:
        total += target

print(total)