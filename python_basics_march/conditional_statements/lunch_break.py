from math import ceil
name_movie = input()
time_movie = int(input())
time_break = int(input())
time_lunch = 0.125 * time_break
time_relax = 0.25 * time_break
total_time = time_relax + time_lunch + time_movie
left_time = ceil(time_break - total_time)
needed_time = ceil(total_time - time_break)
if total_time <= time_break:
    print(f'You have enough time to watch {name_movie} and left with {left_time} minutes free time.')
elif total_time > time_break:
    print(f"You don't have enough time to watch {name_movie}, you need {needed_time} more minutes.")
