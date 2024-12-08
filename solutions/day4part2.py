with open("../inputs/input4.txt", "r") as file:
    data = file.read()

board = data.splitlines()
count = 0
row = 0
col = 0
num_rows = len(board)
num_cols = len(board[0])

chars = {"M", "S"}

while row < num_rows:
    if board[row][col] == "A":
        if row - 1 >= 0 and col - 1 >= 0 and row + 1 < num_rows and col + 1 < num_cols:
            top_left = board[row-1][col-1]
            top_right = board[row-1][col+1]
            bottom_left = board[row+1][col-1]
            bottom_right = board[row+1][col+1]

            if top_left in chars and top_right in chars and bottom_left in chars and bottom_right in chars:
                if top_left != bottom_right and top_right != bottom_left:
                    count += 1

    col += 1
    if col == num_cols:
        col = 0
        row += 1


print(count)