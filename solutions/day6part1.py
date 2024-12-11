with open("../inputs/input6.txt", "r") as file:
    data = file.read()

board = data.splitlines()

row = 0
col = 0
chars = {".", "#"}

while row < len(board):
    if board[row][col] not in chars:
        break
    col += 1
    if col == len(board[row]):
        col = 0
        row += 1

if board[row][col] == "^":
    direction = (-1, 0)
elif board[row][col] == ">":
    direction = (0, 1)
elif board[row][col] == "<":
    direction = (0, -1)
else:
    direction = (1, 0)

positions = {(row, col)}

while 0 <= row < len(board) and 0 <= col < len(board[row]):
    new_row = row + direction[0]
    new_col = col + direction[1]
    if 0 <= new_row < len(board) and 0 <= new_col < len(board[row]):
        if board[new_row][new_col] == ".":
            positions.add((new_row, new_col))
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
                positions.add((new_row, new_col))

    row = new_row
    col = new_col

print(len(positions))