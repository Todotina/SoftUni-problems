size = int(input())
matrix = []
for _ in range(size):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)
command = input()
while command != "END":
    current_command = command.split()
    action, c_row, col, value = current_command[0], int(current_command[1]), int(current_command[2]), int(current_command[3])
    if c_row > size - 1 or col > size - 1 or c_row < 0 or col < 0:
        print("Invalid coordinates")
    else:
        if action == "Add":
            matrix[c_row][col] += value
        elif action == "Subtract":
            matrix[c_row][col] -= value
    command = input()
for row in matrix:
    print(f'{" ".join(str(x) for x in row)}')