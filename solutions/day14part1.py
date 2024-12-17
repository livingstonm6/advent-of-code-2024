with open("../inputs/input14.txt", "r") as file:
    data = file.read()

velocities = []
positions = []

num_cols = 101
num_rows = 103

for robot in data.splitlines():
    p = robot.lstrip("p=").split(" ")[0].split(",")
    p_col = int(p[0])
    p_row = int(p[1])

    v = robot.split("v=")[1].split(",")
    v_col = int(v[0])
    v_row = int(v[1])

    velocities.append([v_col, v_row])
    positions.append([p_col, p_row])

for _ in range(100):
    for i in range(len(velocities)):
        positions[i][0] = (positions[i][0] + velocities[i][0]) % num_cols
        positions[i][1] = (positions[i][1] + velocities[i][1]) % num_rows

mid_row = num_rows // 2
mid_col = num_cols // 2
quadrants = [0, 0, 0, 0]

for position in positions:
    if position[0] < mid_col and position[1] < mid_row:
        quadrants[0] += 1
    elif position[0] < mid_col and position[1] > mid_row:
        quadrants[1] += 1
    elif position[0] > mid_col and position[1] < mid_row:
        quadrants[2] += 1
    elif position[0] > mid_col and position[1] > mid_row:
        quadrants[3] += 1

result = 1
for quadrant in quadrants:
    result *= quadrant

print(result)