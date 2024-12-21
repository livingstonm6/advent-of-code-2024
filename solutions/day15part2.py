with open("../inputs/input15.txt", "r") as file:
    data = file.read().split("\n\n")

old_board = data[0].splitlines()
moves = data[1].replace("\n", "")

robot_position = [0, 0]
board = []

for row in range(len(old_board)):
    board.append([])
    for col in range(len(old_board[0])):
        if old_board[row][col] == "@":
            robot_position = [row, len(board[row])]
            board[row] += ['@', '.']
        elif old_board[row][col] == "#":
            board[row] += ["#", "#"]
        elif old_board[row][col] == "O":
            board[row] += ['[', ']']
        else:
            board[row] += ['.', '.']

num_rows = len(board)
num_cols = len(board[0])

to_move = []

def recur(r_row, r_col, v_dir):
    if board[r_row + v_dir][r_col] == "#":
        return False

    if board[r_row][r_col] == "@":
        if board[r_row + v_dir][r_col] == "[":
            return recur(r_row + v_dir, r_col, v_dir)
        elif board[r_row + v_dir][r_col] == "]":
            return recur(r_row + v_dir, r_col - 1, v_dir)
        return True

    # Box case
    if board[r_row + v_dir][r_col + 1] == "#":
        return False

    if (r_row, r_col) not in to_move:
        to_move.append((r_row, r_col))

    if board[r_row + v_dir][r_col] == "[":
        return recur(r_row + v_dir, r_col, v_dir)
    elif board[r_row + v_dir][r_col] == "]":
        if board[r_row + v_dir][r_col + 1] == "[":
            return recur(r_row + v_dir, r_col - 1, v_dir) and recur(r_row + v_dir, r_col + 1, v_dir)
        return recur(r_row + v_dir, r_col - 1, v_dir)

    if board[r_row + v_dir][r_col + 1] == "[":
        return recur(r_row + v_dir, r_col + 1, v_dir)

    return True

for i in range(len(moves)):
    to_move.clear()
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

    if board[new_position[0]][new_position[1]] == "#":
        continue

    if moves[i] in {"<", ">"}:
        row = new_position[0]
        col = new_position[1]
        while board[row][col] in {'[', ']'}:
            col += 2 * direction[1]
        if board[row][col] == "#":
            continue
        for j in range(col, robot_position[1], -direction[1]):
            board[row][j] = board[row][j - direction[1]]
        board[row][new_position[1]] = "."
    else:
        if recur(robot_position[0], robot_position[1], direction[0]):
            for box in sorted(to_move)[::-direction[0]]:
                board[box[0] + direction[0]][box[1]] = "["
                board[box[0] + direction[0]][box[1] + 1] = "]"
                board[box[0]][box[1]] = "."
                board[box[0]][box[1] + 1] = "."
        else:
            continue

    board[robot_position[0]][robot_position[1]] = "."
    board[new_position[0]][new_position[1]] = "@"
    robot_position = new_position

total = 0
for row in range(num_rows):
    for col in range(num_cols):
        if board[row][col] == "[":
            total += (100 * row) + col

print(total)
