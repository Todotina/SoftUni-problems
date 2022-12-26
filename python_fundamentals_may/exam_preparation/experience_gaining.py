experience_needed = float(input())
count_of_battles = int(input())
total_experience = 0
battle_count = 0
for battle in range(1, count_of_battles + 1):
    experience_current_battle = float(input())
    if battle % 3 == 0:
        experience_current_battle = 1.15 * experience_current_battle
    if battle % 5 == 0:
        experience_current_battle = 0.9 * experience_current_battle
    if battle % 15 == 0:
        experience_current_battle = experience_current_battle * 1.05
    total_experience += experience_current_battle
    battle_count += 1
    if total_experience >= experience_needed:
        print(f"Player successfully collected his needed experience for {battle_count} battles.")
        break

if total_experience < experience_needed:
    print(f"Player was not able to collect the needed experience, {experience_needed - total_experience:.2f} more needed.")