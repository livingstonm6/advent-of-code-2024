with open("../inputs/input15.txt", "r") as file:
    data = file.read().split("\n\n")

board = data[0].splitlines()
moves = data[1].replace("\n", "")

num_rows = len(board)
num_cols = len(board[0])

robot_position = [0, 0]
walls = set()
boxes = set()

for row in range(num_rows):
    for col in range(num_cols):
        if board[row][col] == "@":
            board[row] = board[row][:col] + '.' + board[row][col+1:]
            robot_position = [row, col]
        elif board[row][col] == "#":
            walls.add((row, col))
        elif board[row][col] == "O":
            boxes.add((row, col))

for i in range(len(moves)):
    match moves[i]:
        case "^":
            direction = (-1, 0)
        case "v":
            direction = (1, 0)
        case ">":
            direction = (0, 1)
        case _:
            direction = (0, -1)
    new_position = (robot_position[0] + direction[0], robot_position[1] + direction[1])
    if new_position in walls:
        continue

    to_move = []
    box_position = [new_position[0], new_position[1]]
    while tuple(box_position) in boxes:
        to_move.append(box_position.copy())
        box_position[0] += direction[0]
        box_position[1] += direction[1]
        continue

    if tuple(box_position) in walls:
        continue

    for box in to_move[::-1]:
        boxes.remove(tuple(box))
        boxes.add((box[0] + direction[0], box[1] + direction[1]))

    robot_position = new_position

total = 0
for box in boxes:
    total += (100 * box[0]) + box[1]

print(total)
