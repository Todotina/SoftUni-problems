rows, cols = [int(x) for x in input().split()]
matrix = []
sum_elements = 0
sub_matrix = []
largest_sub_matrix = []
for _ in range(rows):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)
for row in range(rows - 2):
    for col in range(cols - 2):
        current_element = matrix[row][col]
        next_element = matrix[row][col+1]
        next_next_element = matrix[row][col+2]
        below_element = matrix[row+1][col]
        below_next_element = matrix[row+1][col+1]
        further_element = matrix[row+1][col+2]
        below_next_next_element = matrix[row+2][col]
        another_element = matrix[row+2][col+1]
        last_element = matrix[row+2][col+2]
        sub_matrix.append(current_element)
        sub_matrix.append(next_element)
        sub_matrix.append(next_next_element)
        sub_matrix.append(below_element)
        sub_matrix.append(below_next_element)
        sub_matrix.append(further_element)
        sub_matrix.append(below_next_next_element)
        sub_matrix.append(another_element)
        sub_matrix.append(last_element)
        current_sum = sum(sub_matrix)
        if current_sum > sum_elements:
            sum_elements = current_sum
            largest_sub_matrix.append(sub_matrix)
        sub_matrix = []
print(f'Sum = {sum_elements}')
print(f'{" ".join(str(element) for element in largest_sub_matrix[-1][:3])}')
print(f'{" ".join(str(element) for element in largest_sub_matrix[-1][3:6])}')
print(f'{" ".join(str(element) for element in largest_sub_matrix[-1][6:9])}')
