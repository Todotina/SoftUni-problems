size = 6
matrix = []
rover = ()
water = 0
metal = 0
concrete = 0
for r in range(size):
    current_r = input().split()
    if "E" in current_r:
        c = current_r.index("E")
        rover = (r, c)
    matrix.append(current_r)

directions = {
    'up': (- 1, 0),
    'down': (+ 1, 0),
    'left': (0, - 1),
    'right': (0, + 1)
}

rover_broken = False


def check_coordinates(row, col):
    if row == size:
        row = 0
    elif row < 0:
        row = size -1
    if col == size:
        col = 0
    elif col< 0:
        col = size - 1
    return row, col


def position_check(row, col):
    global concrete, metal, water, rover_broken
    if matrix[row][col] == "C":
        concrete += 1
        print(f"Concrete deposit found at ({row}, {col})")
    elif matrix[row][col] == "M":
        metal += 1
        print(f"Metal deposit found at ({row}, {col})")
    elif matrix[row][col] == "W":
        water += 1
        print(f"Water deposit found at ({row}, {col})")
    elif matrix[row][col] == "R":
        rover_broken = True


row, col = rover[0], rover[1]
commands = input().split(", ")
for command in range(len(commands)):
    current_command = commands[command]
    if current_command == 'up':
        row, col = row + directions['up'][0], col + directions['up'][1]
        row, col = check_coordinates(row, col)
        position_check(row, col)
        if rover_broken:
            print(f"Rover got broken at ({row}, {col})")
            break
    elif current_command == 'down':
        row, col = row + directions['down'][0], col + directions['down'][1]
        row, col = check_coordinates(row, col)
        position_check(row, col)
        if rover_broken:
            print(f"Rover got broken at ({row}, {col})")
            break
    elif current_command == 'left':
        row, col = row + directions['left'][0], col + directions['left'][1]
        row, col = check_coordinates(row, col)
        position_check(row, col)
        if rover_broken:
            print(f"Rover got broken at ({row}, {col})")
            break
    elif current_command == 'right':
        row, col = row + directions['right'][0], col + directions['right'][1]
        row, col = check_coordinates(row, col)
        position_check(row, col)
        if rover_broken:
            print(f"Rover got broken at ({row}, {col})")
            break

if metal > 0 and water > 0 and concrete > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")