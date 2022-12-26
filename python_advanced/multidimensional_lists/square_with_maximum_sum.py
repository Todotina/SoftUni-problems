rows, cols = [int(x) for x in input().split(", ")]
matrix = []
sum_elements = 0
sub_matrix = []
largest_sub_matrix = []
for _ in range(rows):
    current_row = [int(x) for x in input().split(", ")]
    matrix.append(current_row)
for row in range(rows - 1):
    for col in range(cols - 1):
        current_element = matrix[row][col]
        next_element = matrix[row][col+1]
        below_element = matrix[row+1][col]
        below_next_element = matrix[row+1][col+1]
        current_sum = current_element + next_element + below_element + below_next_element
        if current_sum > sum_elements:
            sum_elements = current_sum
            sub_matrix.append(current_element)
            sub_matrix.append(next_element)
            sub_matrix.append(below_element)
            sub_matrix.append(below_next_element)
            largest_sub_matrix.append(sub_matrix)
            sub_matrix = []
print(f'{" ".join(str(element) for element in largest_sub_matrix[-1][:2])}')
print(f'{" ".join(str(element) for element in largest_sub_matrix[-1][2:4])}')
print(sum_elements)