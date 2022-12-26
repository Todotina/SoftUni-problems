presents = int(input())
size = int(input())
matrix = []
c_row = 0
c_col = 0
nice_kids = 0
handed_presents_nice_kids = 0
handed_presents_naughty_kids = 0
for _ in range(size):
    current_row = input().split()
    matrix.append(current_row)
for row in range(size):
    for col in range(size):
        if matrix[row][col] == "S":
            c_row = row
            c_col = col
        elif matrix[row][col] == "V":
            nice_kids += 1


def check_presents(count):
    if count <= 0:
        return True


def check_right(a, b):
    if matrix[a][b+1] == "V":
        matrix[a][b + 1] = "-"
        return True
    elif matrix[a][b+1] == "X":
        matrix[a][b + 1] = "-"
        return False


def check_down(a, b):
    if matrix[a+1][b] == "V":
        matrix[a + 1][b] = "-"
        return True
    elif matrix[a+1][b] == "X":
        matrix[a + 1][b] = "-"
        return False


def check_up(a, b):
    if matrix[a-1][b] == "V":
        matrix[a - 1][b] = "-"
        return True
    elif matrix[c_row-2][c_col] == "X":
        matrix[a - 1][b] = "-"
        return False


def check_left(a, b):
    if matrix[a][b-1] == "V":
        matrix[a][b - 1] = "-"
        return True
    elif matrix[a][b-1] == "X":
        matrix[a][b - 1] = "-"
        return False

command = input()
while command:
    if command == "right":
        if matrix[c_row][c_col+1] == "V":
            handed_presents_nice_kids += 1
            presents -= 1
        elif matrix[c_row][c_col+1] == "C":
            if check_right(c_row, c_col+1):
                presents -= 1
                handed_presents_nice_kids += 1
            else:
                presents -= 1
                handed_presents_naughty_kids += 1
            if check_down(c_row, c_col+1):
                presents -= 1
                handed_presents_nice_kids += 1
            else:
                presents -= 1
                handed_presents_naughty_kids += 1
            if check_up(c_row, c_col+1):
                presents -= 1
                handed_presents_nice_kids += 1
            else:
                presents -= 1
                handed_presents_naughty_kids += 1
            if check_left(c_row, c_col+1):
                presents -= 1
                handed_presents_nice_kids += 1
            else:
                presents -= 1
                handed_presents_naughty_kids += 1
        matrix[c_row][c_col + 1] = "S"
        matrix[c_row][c_col] = "-"
        c_col = c_col + 1
    elif command == "down":
        if matrix[c_row+1][c_col] == "V":
            handed_presents_nice_kids += 1
            presents -= 1
        elif matrix[c_row+1][c_col] == "C":
            if check_right(c_row+1, c_col):
                presents -= 1
                handed_presents_nice_kids += 1
            else:
                presents -= 1
                handed_presents_naughty_kids += 1
            if check_down(c_row+1, c_col):
                presents -= 1
                handed_presents_nice_kids += 1
            else:
                presents -= 1
                handed_presents_naughty_kids += 1
            if check_up(c_row+1, c_col):
                presents -= 1
                handed_presents_nice_kids += 1
            else:
                presents -= 1
                handed_presents_naughty_kids += 1
            if check_left(c_row+1, c_col):
                presents -= 1
                handed_presents_nice_kids += 1
            else:
                presents -= 1
                handed_presents_naughty_kids += 1
        matrix[c_row+1][c_col] = "S"
        matrix[c_row][c_col] = "-"
        c_row = c_row + 1
    elif command == "up":
        if matrix[c_row-1][c_col] == "V":
            handed_presents_nice_kids += 1
            presents -= 1
        elif matrix[c_row-1][c_col] == "C":
            if check_right(c_row-1, c_col):
                presents -= 1
                handed_presents_nice_kids += 1
            else:
                presents -= 1
                handed_presents_naughty_kids += 1
            if check_down(c_row-1, c_col):
                presents -= 1
                handed_presents_nice_kids += 1
            else:
                presents -= 1
                handed_presents_naughty_kids += 1
            if check_up(c_row-1, c_col):
                presents -= 1
                handed_presents_nice_kids += 1
            else:
                presents -= 1
                handed_presents_naughty_kids += 1
            if check_left(c_row-1, c_col):
                presents -= 1
                handed_presents_nice_kids += 1
            else:
                presents -= 1
                handed_presents_naughty_kids += 1
        matrix[c_row-1][c_col] = "S"
        matrix[c_row][c_col] = "-"
        c_row = c_row -1
    elif command == "left":
        if matrix[c_row][c_col-1] == "V":
            handed_presents_nice_kids += 1
            presents -= 1
        elif matrix[c_row][c_col-1] == "C":
            if check_right(c_row, c_col-1):
                presents -= 1
                handed_presents_nice_kids += 1
            else:
                presents -= 1
                handed_presents_naughty_kids += 1
            if check_down(c_row, c_col-1):
                presents -= 1
                handed_presents_nice_kids += 1
            else:
                presents -= 1
                handed_presents_naughty_kids += 1
            if check_up(c_row, c_col-1):
                presents -= 1
                handed_presents_nice_kids += 1
            else:
                presents -= 1
                handed_presents_naughty_kids += 1
            if check_left(c_row, c_col-1):
                presents -= 1
                handed_presents_nice_kids += 1
            else:
                presents -= 1
                handed_presents_naughty_kids += 1
        matrix[c_row][c_col - 1] = "S"
        matrix[c_row][c_col] = "-"
        c_col = c_col - 1
    elif command == "Christmas morning" or check_presents(presents):
        break
    command = input()
difference = nice_kids - handed_presents_nice_kids
if presents <= 0 and difference > 0:
    print("Santa ran out of presents!")
for element in matrix:
    print(f'{" ".join(str(x) for x in element)}')
if difference == 0:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {difference} nice kid/s.")
