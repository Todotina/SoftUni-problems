actor_name = input()
academy_points = float(input())
count_jury = int(input())
total_points = academy_points
for people in range(1, count_jury + 1):
    current_name = input()
    points = float(input())
    additional_points = (len(current_name) * points) / 2
    total_points = total_points + additional_points
    if total_points >= 1250.5:
        break
if total_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - total_points:.1f} more!")