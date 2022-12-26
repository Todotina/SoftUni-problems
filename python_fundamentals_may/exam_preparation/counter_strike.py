initial_energy = int(input())
command = input()
end_energy = initial_energy
won_battles = 0
while command != "End of battle":
    distance = int(command)
    if end_energy >= distance:
        won_battles += 1
        end_energy -= distance
        if won_battles % 3 == 0:
            end_energy += won_battles
    elif end_energy < distance:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {end_energy} energy")
        break
    command = input()

if command == "End of battle":
    print(f"Won battles: {won_battles}. Energy left: {end_energy}")

# Every third won battle increases your energy with the value of your current count of won battles.