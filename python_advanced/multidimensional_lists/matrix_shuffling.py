rows, cols = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    current_row = input().split()
    matrix.append(current_row)

command = input()
while command != "END":
    current_command = command.split()
    if len(current_command) != 5:
        print("Invalid input!")
        command = input()
        continue
    action = current_command[0]
    row_one, col_one, row_two, col_two = int(current_command[1]), int(current_command[2]), int(current_command[3]), int(current_command[4])
    if action != 'swap' or row_one < 0 or col_one < 0 or row_two < 0 or col_two < 0:
        print("Invalid input!")
        continue
    if row_one <= rows -1 and row_two <= rows -1 and col_one <= cols -1 and col_two <= cols -1:
        first_old_value = matrix[row_one][col_one]
        second_old_value = matrix[row_two][col_two]
        matrix[row_one][col_one] = second_old_value
        matrix[row_two][col_two] = first_old_value
        for element in matrix:
            print(f'{" ".join(str(x) for x in element)}')
    else:
        print("Invalid input!")
    command = input()