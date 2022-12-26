first_game = input()
second_game = input()
third_game = input()
count_won_games = 0
count_lost_games = 0
count_drawn_games = 0

if int(first_game[0]) > int(first_game[2]):
    count_won_games += 1
elif int(first_game[0]) < int(first_game[2]):
    count_lost_games += 1
elif int(first_game[0]) == int(first_game[2]):
    count_drawn_games += 1
if int(second_game[0]) > int(second_game[2]):
    count_won_games += 1
elif int(second_game[0]) < int(second_game[2]):
    count_lost_games += 1
elif int(second_game[0]) == int(second_game[2]):
    count_drawn_games += 1
if int(third_game[0]) > int(third_game[2]):
    count_won_games += 1
elif int(third_game[0]) < int(third_game[2]):
    count_lost_games += 1
elif int(third_game[0]) == int(third_game[2]):
    count_drawn_games += 1

print(f"Team won {count_won_games} games.")
print(f"Team lost {count_lost_games} games.")
print(f"Drawn games: {count_drawn_games}")