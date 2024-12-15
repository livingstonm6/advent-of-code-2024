with open("../inputs/input10.txt", "r") as file:
    data = file.read().strip()

board = data.splitlines()
stack = [0]
endpoints = set()

def dfs(row, col):
    if len(stack) == 10:
        endpoints.add((row, col))
        return
    # up
    if row > 0 and int(board[row-1][col]) == stack[-1] + 1:
        stack.append(int(board[row-1][col]))
        dfs(row-1, col)
        stack.pop()

    # down
    if row < len(board) - 1 and int(board[row+1][col]) == stack[-1] + 1:
        stack.append(int(board[row+1][col]))
        dfs(row+1, col)
        stack.pop()

    # left
    if col > 0 and int(board[row][col-1]) == stack[-1] + 1:
        stack.append(int(board[row][col-1]))
        dfs(row, col-1)
        stack.pop()

    # right
    if col < len(board[0]) - 1 and int(board[row][col+1]) == stack[-1] + 1:
        stack.append(int(board[row][col+1]))
        dfs(row, col+1)
        stack.pop()

total = 0

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == "0":
            dfs(i, j)
            total += len(endpoints)
            endpoints.clear()

print(total)
