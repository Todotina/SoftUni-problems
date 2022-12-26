players = input().split(", ")
size = 6
maze = []
first_player = players[0]
second_player = players[1]

for _ in range(size):
    current_row = input().split(" ")
    maze.append(current_row)

players_and_positions = []
hit_wall = {}
turn = 0

while True:
    coordinates = input()
    players_and_positions.append(coordinates)
    position_player = maze[int(coordinates[1])][int(coordinates[4])]
    if len(players_and_positions) % 2 != 0:
        player = first_player
        other_player = second_player
        turn += 1
    else:
        player = second_player
        other_player = first_player
        turn += 1
    if player not in hit_wall:
        hit_wall[player] = []
    if len(hit_wall[player]) > 0 and hit_wall[player][-1] == turn - 2:
        continue
    if position_player == "E":
        print(f"{player} found the Exit and wins the game!")
        break
    elif position_player == "T":
        print(f"{player} is out of the game! The winner is {other_player}.")
        break
    elif position_player == "W":
        print(f"{player} hits a wall and needs to rest.")
        hit_wall[player].append(turn)

