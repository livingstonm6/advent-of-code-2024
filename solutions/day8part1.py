def distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

with open("../inputs/input8.txt", "r") as file:
    data = file.read()

board = data.splitlines()

row = 0
col = 0

num_rows = len(board)
num_cols = len(board[0])

antennas = {}

while row < num_rows:
    element = board[row][col]
    if element != ".":
        if element in antennas:
            antennas[element].append((row, col))
        else:
            antennas[element] = [(row, col)]

    col += 1
    if col == num_cols:
        row += 1
        col = 0

anti_nodes = set()

for _, points in antennas.items():
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            point1 = points[i]
            point2 = points[j]

            start_row_diff = point1[0] - point2[0]
            start_col_diff = point1[1] - point2[1]

            row_diff = start_row_diff
            col_diff = start_col_diff

            row = point2[0] + row_diff
            col = point2[1] + col_diff

            while 0 <= row < num_rows and 0 <= col < num_cols:
                if (row, col) != point2 and (distance((row, col), point1) / distance((row, col), point2)) in {2, 0.5}:
                    anti_nodes.add((row, col))
                row += row_diff
                col += col_diff

            row_diff = start_row_diff
            col_diff = start_col_diff

            row = point1[0] - row_diff
            col = point1[1] - col_diff

            while 0 <= row < num_rows and 0 <= col < num_cols:
                if (row, col) != point2 and (distance((row, col), point1) / distance((row, col), point2)) in {2, 0.5}:
                    anti_nodes.add((row, col))
                row -= row_diff
                col -= col_diff

print(len(anti_nodes))
