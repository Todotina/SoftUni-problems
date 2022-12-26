import math
count_tournaments = int(input())
initial_points = int(input())
final_points = initial_points
won_tournaments = 0
for tournaments in range(1, count_tournaments + 1):
    current_tournament = input()
    if current_tournament == "W":
        final_points += 2000
        won_tournaments += 1
    elif current_tournament == "F":
        final_points += 1200
    elif current_tournament == "SF":
        final_points += 720
average_points = math.floor((final_points - initial_points) / count_tournaments)
print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{won_tournaments/count_tournaments * 100:.2f}%")