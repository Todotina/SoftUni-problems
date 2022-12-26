def create(direction, value):
    r, c = current_position[0] + directions[direction][0], current_position[1] + directions[direction][1]
    if matrix[r][c] == ".":
        matrix[r][c] = value
    return r, c

def update(direction, value):
    r, c = current_position[0] + directions[direction][0], current_position[1] + directions[direction][1]
    if matrix[r][c] != ".":
        matrix[r][c] = value
    return r, c

def delete(direction):
    r, c = current_position[0] + directions[direction][0], current_position[1] + directions[direction][1]
    if matrix[r][c] != ".":
        matrix[r][c] = "."
    return r, c

def read(direction):
    r, c = current_position[0] + directions[direction][0], current_position[1] + directions[direction][1]
    if matrix[r][c] != ".":
        print(matrix[r][c])
    return r, c

size = 6
directions = {
    'up': (- 1, 0),
    'down': (+ 1, 0),
    'right': (0, + 1),
    'left': (0, -1)
}
matrix = []
for row in range(size):
    current_row = input().split()
    matrix.append(current_row)

first_position = input().split(", ")
f_row, f_col = first_position
first_row = int(f_row[1])
first_col = int(f_col[0])
current_position = [first_row, first_col]
command = input()

while command != "Stop":
    current_command = command.split(", ")
    action, direction = current_command[0], current_command[1]
    if len(current_command) == 3:
        value = current_command[2]
    if action == "Create":
        current_position = create(direction, value)
    elif action == "Update":
        current_position = update(direction, value)
    elif action == "Delete":
        current_position = delete(direction)
    elif action == "Read":
        current_position = read(direction)

    command = input()

for r in matrix:
    print(f'{" ".join(str(x) for x in r)}')