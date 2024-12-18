with open("../inputs/input14.txt", "r") as file:
    data = file.read()

velocities = []
positions = []

num_cols = 101
num_rows = 103

output = open("output14.txt", "w")

for robot in data.splitlines():
    p = robot.lstrip("p=").split(" ")[0].split(",")
    p_col = int(p[0])
    p_row = int(p[1])

    v = robot.split("v=")[1].split(",")
    v_col = int(v[0])
    v_row = int(v[1])

    velocities.append([v_col, v_row])
    positions.append([p_col, p_row])

# First, submit guesses into the Advent of Code site to narrow down the range (1000, 5000, 10000, etc.).
# It will tell you if the answer is higher or lower than your guess for the first few attempts.
# Then, write the iterations within that range to a text file and scroll through it until you find the Christmas tree.
# The answer is the iteration number of the board containing the Christmas tree.

for iteration in range(1, 8000):
    board = [['.' for _ in range(num_cols)] for _ in range(num_rows)]
    print("Iteration", iteration)
    output.write("Iteration {}\n".format(iteration))
    for i in range(len(velocities)):
        positions[i][0] = (positions[i][0] + velocities[i][0]) % num_cols
        positions[i][1] = (positions[i][1] + velocities[i][1]) % num_rows
        if board[positions[i][1]][positions[i][0]] == '.':
            board[positions[i][1]][positions[i][0]] = 1
        else:
            board[positions[i][1]][positions[i][0]] += 1

    for row in range(num_rows):
        for col in range(num_cols):
            output.write(str(board[row][col]))
        output.write("\n")
    output.write("\n")

output.close()