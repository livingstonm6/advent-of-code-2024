with open("../inputs/input12.txt", "r") as file:
    data = file.read().strip()

board = data.splitlines()

visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

def dfs(row, col):
    visited[row][col] = True
    area = 1
    perimeter = 0

    # up
    if row > 0:
        if board[row - 1][col] != board[row][col]:
            perimeter += 1
        elif not visited[row - 1][col]:
            up_area, up_perimeter = dfs(row - 1, col)
            area += up_area
            perimeter += up_perimeter
    else:
        perimeter += 1

    # right
    if col < len(board[0]) - 1:
        if board[row][col + 1] != board[row][col]:
            perimeter += 1
        elif not visited[row][col + 1]:
            right_area, right_perimeter = dfs(row, col + 1)
            area += right_area
            perimeter += right_perimeter
    else:
        perimeter += 1

    # down
    if row < len(board) - 1:
        if board[row + 1][col] != board[row][col]:
            perimeter += 1
        elif not visited[row + 1][col]:
            down_area, down_perimeter = dfs(row + 1, col)
            area += down_area
            perimeter += down_perimeter
    else:
        perimeter += 1

    # left
    if col > 0:
        if board[row][col - 1] != board[row][col]:
            perimeter += 1
        elif not visited[row][col - 1]:
            left_area, left_perimeter = dfs(row, col - 1)
            area += left_area
            perimeter += left_perimeter
    else:
        perimeter += 1

    return area, perimeter

total = 0
for y in range(len(board)):
    for x in range(len(board[0])):
        if not visited[y][x]:
            block_area, block_perimeter = dfs(y, x)
            total += block_area * block_perimeter

print(total)
