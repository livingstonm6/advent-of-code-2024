with open("../inputs/input17.txt", "r") as file:
    data = file.read().split("\n\n")

register_values = [int(x.split(": ")[1]) for x in data[0].splitlines()]

a = register_values[0]
b = register_values[1]
c = register_values[2]

opcodes = [int(x) for x in data[1].split(" ")[1].split(",")]

output = []

def get_combo_value(operand):
    match operand:
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c
        case _:
            return operand

i = 0
while i + 1 < len(opcodes):
    current = opcodes[i]
    operand = opcodes[i + 1]

    match current:
        case 0:
            numerator = a
            denominator = 2 ** get_combo_value(operand)
            a = numerator // denominator
        case 1:
            b ^= operand
        case 2:
            b = get_combo_value(operand) % 8
        case 3:
            if a != 0:
                i = operand
                continue
        case 4:
            b ^= c
        case 5:
            output.append(str(get_combo_value(operand) % 8))
        case 6:
            numerator = a
            denominator = 2 ** get_combo_value(operand)
            b = numerator // denominator
        case 7:
            numerator = a
            denominator = 2 ** get_combo_value(operand)
            c = numerator // denominator

    i += 2

print(",".join(output))