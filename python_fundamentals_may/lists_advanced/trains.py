number_of_wagons = int(input())
wagon_list = [0] * number_of_wagons
command = input()

while command != "End":
    command_list = command. split(" ")
    action = command_list[0]
    if action == "add":
        people = command_list[1]
        wagon_list[-1] += int(people)
    elif action == "insert":
        people = command_list[2]
        index = command_list[1]
        wagon_list[int(index)] += int(people)
    elif action == "leave":
        people = command_list[2]
        index = command_list[1]
        wagon_list[int(index)] -= int(people)
    command = input()
if command == "End":
    print(wagon_list)

    # • "add {people}" – you should add the number of people in the last wagon
    # • "insert {index} {people}" - you should add the number of people at the given wagon
    # • "leave {index} {people}" - you should remove the number of people from the wagon.