stops = input()
instruction = input()
list_with_stops = [stops]


def valid_index(string, index):
    if 0 <= index < len(string):
        return True
    return False


while instruction != "Travel":
    command = instruction.split(":")
    action = command[0]
    if action == "Add Stop":
        index, string = int(command[1]), command[2]
        if valid_index(list_with_stops[-1], index):
            beginning = list_with_stops[-1][:index]
            end = list_with_stops[-1][index:]
            modified_stops = beginning + string + end
            list_with_stops.append(modified_stops)
        print(list_with_stops[-1])
    elif action == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        if valid_index(list_with_stops[-1], start_index) and valid_index(list_with_stops[-1], end_index):
            modified_stops = list_with_stops[-1].replace(list_with_stops[-1][start_index:end_index + 1], "")
            list_with_stops.append(modified_stops)
        print(list_with_stops[-1])
    elif action == "Switch":
        old_string, new_string = command[1], command[2]
        if old_string in list_with_stops[-1]:
            modified_stops = list_with_stops[-1].replace(old_string, new_string, list_with_stops[-1].count(old_string))
            list_with_stops.append(modified_stops)
        print(list_with_stops[-1])

    instruction = input()

print(f"Ready for world tour! Planned stops: {list_with_stops[-1]}")