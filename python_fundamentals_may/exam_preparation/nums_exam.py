def value_check(number):
    if number in list_of_numbers:
        return True


# def collapse(number):
#     for element in updated_list:
#         if element < number:
#             updated_list.remove(element)


list_of_numbers = [int(number) for number in input().split(" ")]
updated_list = []
command = input()

while command != "Finish":
    current_command_list = command.split(" ")
    action = current_command_list[0]
    value = int(current_command_list[1])
    if action == "Add":
        list_of_numbers.append(value)
    elif action == "Remove":
        if value_check(value):
            list_of_numbers.remove(value)
    elif action == "Replace":
        replacement = int(current_command_list[2])
        if value_check(value):
            index = list_of_numbers.index(value)
            list_of_numbers[index] = replacement
    elif action == "Collapse":
        for element in updated_list:
            if element < value:
                list_of_numbers.remove(element)
        # collapse(value)

    updated_list = list_of_numbers.copy()
    list_of_numbers.clear()
    list_of_numbers = updated_list

    command = input()

print(' '.join(map(str, updated_list)))