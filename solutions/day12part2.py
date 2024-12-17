with open("../inputs/input12.txt", "r") as file:
    data = file.read().strip()

board = data.splitlines()
visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
sides = set()

def dfs(row, col):
    visited[row][col] = True
    area = 1

    # up
    if row > 0:
        if board[row - 1][col] != board[row][col]:
            sides.add((row, col, "up"))
        elif not visited[row - 1][col]:
            up_area = dfs(row - 1, col)
            area += up_area
    else:
        sides.add((row, col, "up"))

    # right
    if col < len(board[0]) - 1:
        if board[row][col + 1] != board[row][col]:
            sides.add((row, col, "right"))
        elif not visited[row][col + 1]:
            right_area = dfs(row, col + 1)
            area += right_area
    else:
        sides.add((row, col, "right"))

    # down
    if row < len(board) - 1:
        if board[row + 1][col] != board[row][col]:
            sides.add((row, col, "down"))
        elif not visited[row + 1][col]:
            down_area = dfs(row + 1, col)
            area += down_area
    else:
        sides.add((row, col, "down"))

    # left
    if col > 0:
        if board[row][col - 1] != board[row][col]:
            sides.add((row, col, "left"))
        elif not visited[row][col - 1]:
            left_area = dfs(row, col - 1)
            area += left_area
    else:
        sides.add((row, col, "left"))

    return area

total = 0
for y in range(len(board)):
    for x in range(len(board[0])):
        if not visited[y][x]:
            block_area = dfs(y, x)
            num_sides = 0

            while len(sides) > 0:
                num_sides += 1
                (row, col, side) = sides.pop()
                if side in {"up", "down"}:
                    # left
                    col_i = col
                    while col_i - 1 >= 0 and (row, col_i - 1, side) in sides:
                        col_i -= 1
                        sides.remove((row, col_i, side))

                    # right
                    col_i = col
                    while col_i + 1 < len(board[0]) and (row, col_i + 1, side) in sides:
                        col_i += 1
                        sides.remove((row, col_i, side))

                else:
                    # up
                    row_i = row
                    while row_i - 1 >= 0 and (row_i - 1, col, side) in sides:
                        row_i -= 1
                        sides.remove((row_i, col, side))

                    # down
                    row_i = row
                    while row_i + 1 < len(board) and (row_i + 1, col, side) in sides:
                        row_i += 1
                        sides.remove((row_i, col, side))

            total += block_area * num_sides

print(total)
