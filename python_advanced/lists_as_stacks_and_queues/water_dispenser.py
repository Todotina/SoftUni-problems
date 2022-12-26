from collections import deque

starting_quantity = int(input())
people = deque()

while True:
    command = input()
    if command == "Start":
        break
    people.append(command)

while True:
    line = input()
    if line == "End":
        print(f'{starting_quantity} liters left')
        break
    action = line.split()
    if len(action) == 2:
        liters = int(action[1])
        starting_quantity += liters
    else:
        liters = int(action[0])
        if starting_quantity >= liters:
            print(f'{people.popleft()} got water')
            starting_quantity -= liters
        else:
            print(f'{people.popleft()} must wait')
