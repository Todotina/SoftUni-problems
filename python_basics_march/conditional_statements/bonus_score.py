points = int(input())
bonus_points = 0
if points <= 100:
    bonus_points = 5
elif points <= 1000:
    bonus_points = 0.2 * points
elif points > 1000:
    bonus_points = 0.1 * points
bonus = bonus_points
if points % 2 == 0:
    bonus = bonus_points + 1
elif points % 10 == 5:
    bonus = bonus_points + 2
print(bonus)
print(points + bonus)