command = input()
sum_steps = 0

while command != "Going home":
    steps = int(command)
    sum_steps += steps
    if sum_steps >= 10000:
        break
    command = input()

if command == "Going home":
    steps_to_home = int(input())
    sum_steps += steps_to_home
difference = abs(sum_steps - 10000)
if sum_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")