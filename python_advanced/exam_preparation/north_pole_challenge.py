rows, cols = [int(x) for x in input().split(", ")]
shop = []
position = ()
decorations = 0
gifts = 0
cookies = 0
last_position = ()

for row in range(rows):
    current_row = input().split()
    if "Y" in current_row:
        position = (row, current_row.index("Y"))
    if "D" in current_row:
        decorations += current_row.count("D")
    if "G" in current_row:
        gifts += current_row.count("G")
    if "C" in current_row:
        cookies += current_row.count("C")
    shop.append(current_row)

collected_items = {
    'decorations': 0,
    'gifts': 0,
    'cookies': 0,
}


def coordinates_check(r, c):
    global rows, cols
    if r == rows:
        r = 0
    elif r < 0:
        r = rows - 1
    else:
        r = r
    if c == cols:
        c = 0
    elif c < 0:
        c = cols - 1
    else:
        c = c
    return r, c


def position_check(r, c):
    if shop[r][c] == "D":
        collected_items['decorations'] += 1
    elif shop[r][c] == "G":
        collected_items['gifts'] += 1
    elif shop[r][c] == "C":
        collected_items['cookies'] += 1


shop[position[0]][position[1]] = "x"
command = input()
while command != "End":
    direction, steps = command.split("-")[0], int(command.split("-")[1])
    if direction == 'up':
        for step in range(steps):
            current_position = (position[0] - 1, position[1])
            r, c = coordinates_check(current_position[0], current_position[1])
            position_check(r, c)
            shop[r][c] = "x"
            position = (r, c)
    elif direction == 'down':
        for step in range(steps):
            current_position = (position[0] + 1, position[1])
            r, c = coordinates_check(current_position[0], current_position[1])
            position_check(r, c)
            shop[r][c] = "x"
            position = (r, c)
    elif direction == 'right':
        for step in range(steps):
            current_position = (position[0], position[1] + 1)
            r, c = coordinates_check(current_position[0], current_position[1])
            position_check(r, c)
            shop[r][c] = "x"
            position = (r, c)
    elif direction == 'left':
        for step in range(steps):
            current_position = (position[0], position[1] - 1)
            r, c = coordinates_check(current_position[0], current_position[1])
            position_check(r, c)
            shop[r][c] = "x"
            position = (r, c)
    last_position = position

    if collected_items['decorations'] == decorations and collected_items['gifts'] ==  gifts and collected_items['cookies'] == cookies:
        print("Merry Christmas!")
        break

    command = input()

print("You've collected:")
print(f"- {collected_items['decorations']} Christmas decorations")
print(f"- {collected_items['gifts']} Gifts")
print(f"- {collected_items['cookies']} Cookies")
shop[last_position[0]][last_position[1]] = "Y"
for row in shop:
    print(f"{' '.join(el for el in row)}")