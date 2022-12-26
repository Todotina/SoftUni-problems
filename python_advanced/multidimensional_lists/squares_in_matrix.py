rows, cols = [int(x) for x in input().split()]
matrix = []
count = 0
for _ in range(rows):
    current_row = [x for x in input().split()]
    matrix.append(current_row)
for row in range(rows - 1):
    for col in range(cols - 1):
        current_element = matrix[row][col]
        next_element = matrix[row][col+1]
        below_element = matrix[row+1][col]
        below_next_element = matrix[row+1][col+1]
        if current_element == next_element and current_element == below_element and current_element == below_next_element:
            count += 1
print(count)