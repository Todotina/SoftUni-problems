days = int(input())
raised_money = 0
count_lost_games = 0
count_won_games = 0
days_won = 0
days_lost = 0
for days in range(1, days + 1):
    sport_name = input()
    while sport_name != "Finish":
        current_result = input()
        if current_result == "win":
            raised_money += 20
            count_won_games += 1
        else:
            count_lost_games += 1
        sport_name = input()
    if count_won_games > count_lost_games:
        raised_money *= 1.1
        days_won += 1
    else:
        days_lost += 1

if days_won > days_lost:
    raised_money *= 1.2
    print(f"You won the tournament! Total raised money: {raised_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {raised_money:.2f}")

