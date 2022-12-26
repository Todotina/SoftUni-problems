size = int(input())
matrix = []
knights_to_be_removed = 0
for x in range(size):
    current_row = input()
    sub_matrix = []
    for item in current_row:
        sub_matrix.append(item)
    matrix.append(sub_matrix)
if size >= 3:
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                if col <= size - 3 and row <= size - 3:
                    if matrix[row + 2][col + 1] == "K":
                        knights_to_be_removed += 1
                        matrix[row + 2][col + 1] = 0
                    elif matrix[row + 1][col + 2] == "K":
                        knights_to_be_removed += 1
                        matrix[row + 1][col + 2] = 0
                elif col >= size - 3 and row >= size - 3:
                    if matrix[row - 2][col - 1] == "K":
                        knights_to_be_removed += 1
                        matrix[row - 2][col - 1] = 0
                    elif matrix[row - 1][col - 2] == "K":
                        knights_to_be_removed += 1
                        matrix[row - 1][col - 2] = 0
            else:
                continue

print(knights_to_be_removed)