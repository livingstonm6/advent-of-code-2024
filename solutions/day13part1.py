with open("../inputs/input13.txt", "r") as file:
    data = file.read()

machines = [x.splitlines() for x in data.split("\n\n")]

total_min = 0

for machine in data.split("\n\n"):
    machine_text = machine.splitlines()
    a_x = int(machine_text[0].split("X+")[1].split(",")[0])
    a_y = int(machine_text[0].split("Y+")[1])

    b_x = int(machine_text[1].split("X+")[1].split(",")[0])
    b_y = int(machine_text[1].split("Y+")[1])

    target_x = int(machine_text[2].split("X=")[1].split(",")[0])
    target_y = int(machine_text[2].split("Y=")[1])

    minimum = float('inf')

    for a_presses in range(101):
        for b_presses in range(101):
            if (a_x * a_presses) + (b_x * b_presses) == target_x and (a_y * a_presses) + (b_y * b_presses) == target_y:
                minimum = min(minimum, (3 * a_presses) + b_presses)

    if minimum < float('inf'):
        total_min += minimum

print(total_min)
