with open("../inputs/input13.txt", "r") as file:
    data = file.read()

machines = [x.splitlines() for x in data.split("\n\n")]

total = 0

for machine in data.split("\n\n"):
    machine_text = machine.splitlines()
    a_x = int(machine_text[0].split("X+")[1].split(",")[0])
    a_y = int(machine_text[0].split("Y+")[1])

    b_x = int(machine_text[1].split("X+")[1].split(",")[0])
    b_y = int(machine_text[1].split("Y+")[1])

    target_x = int(machine_text[2].split("X=")[1].split(",")[0]) + 10000000000000
    target_y = int(machine_text[2].split("Y=")[1]) + 10000000000000

    # Gauss Jordan elimination
    target_x /= a_x
    b_y -= (b_x * a_y) / a_x
    target_y -= (target_x * a_y)

    target_y /= b_y
    target_x -= (target_y * b_x) / a_x

    if round(target_x, 3) % 1 == 0 and round(target_y, 3) % 1 == 0:
        total += round((target_x * 3) + target_y, 3)

print(int(total))

