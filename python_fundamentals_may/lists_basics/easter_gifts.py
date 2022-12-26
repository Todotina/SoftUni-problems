list_of_gifts = input().split(" ")
command = input()
while command != "No Money":
    current_command_list = command.split(" ")
    instruction = current_command_list[0]
    gift = current_command_list[1]
    if instruction == "OutOfStock":
        for position in range(len(list_of_gifts)):
            if list_of_gifts[position] == gift:
                list_of_gifts[position] = "None"
    elif instruction == "Required":
        index = int(current_command_list[2])
        if 0 <= index < len(list_of_gifts):
            list_of_gifts[index] = gift
    elif instruction == "JustInCase":
        list_of_gifts[-1] = gift

    command = input()

list_of_gifts = [element for element in list_of_gifts if element != "None"]
print(' '.join(list_of_gifts))