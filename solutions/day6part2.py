with open("../inputs/input6.txt", "r") as file:
    data = file.read()

board = data.splitlines()

start_row = 0
start_col = 0
chars = {".", "#"}

while start_row < len(board):
    if board[start_row][start_col] not in chars:
        break
    start_col += 1
    if start_col == len(board[start_row]):
        start_col = 0
        start_row += 1

if board[start_row][start_col] == "^":
    start_direction = (-1, 0)
elif board[start_row][start_col] == ">":
    start_direction = (0, 1)
elif board[start_row][start_col] == "<":
    start_direction = (0, -1)
else:
    start_direction = (1, 0)

obstacle_row = 0
obstacle_col = 0

total = 0

while obstacle_row < len(board):
    if board[obstacle_row][obstacle_col] == ".":
        board[obstacle_row] = board[obstacle_row][0:obstacle_col] + "#" + board[obstacle_row][obstacle_col+1:]

        row = start_row
        col = start_col
        direction = start_direction
        positions = {(row, col, direction)}

        while 0 <= row < len(board) and 0 <= col < len(board[row]):
            new_row = row + direction[0]
            new_col = col + direction[1]
            if 0 <= new_row < len(board) and 0 <= new_col < len(board[row]):
                if board[new_row][new_col] == ".":
                    position = (new_row, new_col, direction)
                    if position in positions:
                        total += 1
                        break
                    positions.add(position)
                elif board[new_row][new_col] == "#":
                    while board[new_row][new_col] == "#":
                        if direction == (-1, 0):
                            direction = (0, 1)
                        elif direction == (0, 1):
                            direction = (1, 0)
                        elif direction == (1, 0):
                            direction = (0, -1)
                        else:
                            direction = (-1, 0)
                        new_row = row + direction[0]
                        new_col = col + direction[1]

                        if not 0 <= new_row < len(board) or not 0 <= new_col < len(board[row]):
                            break

                    if 0 <= new_row < len(board) and 0 <= new_col < len(board[row]):
                        position = (new_row, new_col, direction)
                        if position in positions:
                            total += 1
                            break
                        positions.add(position)

            row = new_row
            col = new_col

        board[obstacle_row] = board[obstacle_row][0:obstacle_col] + "." + board[obstacle_row][obstacle_col + 1:]

    obstacle_col += 1
    if obstacle_col == len(board[obstacle_row]):
        print("Row", obstacle_row, "of", len(board))
        obstacle_col = 0
        obstacle_row += 1

print(total)