def check_record(levels):
    positive = int(levels[0]) - int(levels[1]) > 0
    safe = True
    for i in range(len(levels) - 1):
        difference = int(levels[i]) - int(levels[i + 1])
        if (difference > 0) != positive:
            safe = False
            break

        difference = abs(difference)
        if difference < 1 or difference > 3:
            safe = False
            break
    return safe



with open("../inputs/input2.txt", "r") as file:
    data = file.read()

total_safe = 0

for record in data.splitlines():
    levels = record.split(" ")
    record_safe = False

    for i in range(len(levels)):
        temp = levels.copy()
        temp.pop(i)
        safe = check_record(temp)
        if safe:
            record_safe = True
            break

    if record_safe:
        total_safe += 1


print(total_safe)


