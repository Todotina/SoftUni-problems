count_sold_games = int(input())
count_hearthstone = 0
count_fornite = 0
count_overwatch = 0
count_others = 0
for games in range(count_sold_games):
    current_game = input()
    if current_game == "Hearthstone":
        count_hearthstone += 1
    elif current_game == "Fornite":
        count_fornite += 1
    elif current_game == "Overwatch":
        count_overwatch += 1
    else:
        count_others += 1

print(f"Hearthstone - {count_hearthstone/count_sold_games * 100:.2f}%")
print(f"Fornite - {count_fornite/count_sold_games * 100:.2f}%")
print(f"Overwatch - {count_overwatch/count_sold_games * 100:.2f}%")
print(f"Others - {count_others/count_sold_games * 100:.2f}%")