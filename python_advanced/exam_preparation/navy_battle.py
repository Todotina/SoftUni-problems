size = int(input())
battlefield = []
position = ()
mine_hits = 0
cruisers = 0

for r in range(size):
    current_row = list(input())
    if "S" in current_row:
        position = (r, current_row.index("S"))
    battlefield.append(current_row)

battlefield[position[0]][position[1]] = "-"
directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'right': (0, +1),
    'left': (0, -1)
}


def position_check(position):
    global cruisers,  mine_hits
    if battlefield[position[0]][position[1]] == "C":
        cruisers += 1
        battlefield[position[0]][position[1]] = "-"
    elif battlefield[position[0]][position[1]] == "*":
        mine_hits += 1
        battlefield[position[0]][position[1]] = "-"
    return cruisers, mine_hits


direction = input()
while direction:
    if direction == 'up':
        position = (position[0] + directions[direction][0], position[1] + directions[direction][1])
        position_check(position)
        if cruisers == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            battlefield[position[0]][position[1]] = "S"
            break
        elif mine_hits == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{position[0]}, {position[1]}]!")
            battlefield[position[0]][position[1]] = "S"
            break
    elif direction == 'down':
        position = (position[0] + directions[direction][0], position[1] + directions[direction][1])
        position_check(position)
        if cruisers == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            battlefield[position[0]][position[1]] = "S"
            break
        elif mine_hits == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{position[0]}, {position[1]}]!")
            battlefield[position[0]][position[1]] = "S"
            break
    elif direction == 'right':
        position = (position[0] + directions[direction][0], position[1] + directions[direction][1])
        position_check(position)
        if cruisers == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            battlefield[position[0]][position[1]] = "S"
            break
        elif mine_hits == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{position[0]}, {position[1]}]!")
            battlefield[position[0]][position[1]] = "S"
            break
    elif direction == 'left':
        position = (position[0] + directions[direction][0], position[1] + directions[direction][1])
        position_check(position)
        if cruisers == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            battlefield[position[0]][position[1]] = "S"
            break
        elif mine_hits == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{position[0]}, {position[1]}]!")
            battlefield[position[0]][position[1]] = "S"
            break

    direction = input()

# battlefield[position[0]][position[1]] = "S"
for row in battlefield:
    string = ''
    for el in row:
        string += el
    print(string)
