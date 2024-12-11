from collections import deque

with open("../inputs/input5.txt", "r") as file:
    data = file.read()

temp = data.split("\n\n")

rules_data = temp[0].splitlines()
updates = temp[1].splitlines()
total = 0
rules = {}

for rule in rules_data:
    temp = rule.split("|")
    if temp[0] not in rules:
        rules[temp[0]] = {temp[1]}
    else:
        rules[temp[0]].add(temp[1])

for update in updates:
    page_nums = update.split(",")
    valid = True
    previous_pages = set()
    for page_num in page_nums:
        rule_set = rules.get(page_num, None)
        if rule_set is not None and len(previous_pages & rule_set) != 0:
            valid = False
            break
        previous_pages.add(page_num)

    if valid:
        continue

    new_order = ["0" for _ in range(len(page_nums))]
    index = len(new_order) - 1
    added = set()

    for page_num in page_nums:
        if page_num not in rules:
            new_order[index] = page_num
            added.add(page_num)
            index -= 1

    update_set = set(page_nums)
    queue = deque(update_set - added)

    while len(queue) > 0:
        page = queue.popleft()
        if rules[page] & update_set <= added:
            new_order[index] = page
            added.add(page)
            index -= 1
        else:
            queue.append(page)

    midpoint = len(new_order) // 2
    total += int(new_order[midpoint])

print(total)