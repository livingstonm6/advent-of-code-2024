with open("../inputs/input4.txt", "r") as file:
    data = file.read()

board = data.splitlines()
count = 0
row = 0
col = 0
num_rows = len(board)
num_cols = len(board[0])

while row < num_rows:
    if board[row][col] == "X":
        # up
        if row - 3 >= 0 and board[row-1][col] == "M" and board[row-2][col] == "A" and board[row-3][col] == "S":
            count += 1

        # down
        if row + 3 < num_rows and board[row+1][col] == "M" and board[row+2][col] == "A" and board[row+3][col] == "S":
            count += 1

        # left
        if col - 3 >= 0 and board[row][col-1] == "M" and board[row][col-2] == "A" and board[row][col-3] == "S":
            count += 1

        # right
        if col + 3 < num_cols and board[row][col+1] == "M" and board[row][col+2] == "A" and board[row][col+3] == "S":
            count += 1

        # up-left
        if row - 3 >= 0 and col - 3 >= 0 and board[row-1][col-1] == "M" and board[row-2][col-2] == "A" and board[row-3][col-3] == "S":
            count += 1

        # up-right
        if row - 3 >= 0 and col + 3 < num_cols and board[row-1][col+1] == "M" and board[row-2][col+2] == "A" and board[row-3][col+3] == "S":
            count += 1

        # down-left
        if row + 3 < num_rows and col - 3 >= 0 and board[row+1][col-1] == "M" and board[row+2][col-2] == "A" and board[row+3][col-3] == "S":
            count += 1

        # down-right
        if row + 3 < num_rows and col + 3 < num_cols and board[row+1][col+1] == "M" and board[row+2][col+2] == "A" and board[row+3][col+3] == "S":
            count += 1

    col += 1
    if col == num_cols:
        col = 0
        row += 1


print(count)