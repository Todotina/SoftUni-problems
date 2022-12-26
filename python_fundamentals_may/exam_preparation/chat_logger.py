def chat(message):
    list_of_commands.append(message)


def delete(message):
    if message in list_of_commands:
        index = list_of_commands.index(message)
        del list_of_commands[index]
    else:
        return False


def edit(message):
    if message in list_of_commands:
        index = list_of_commands.index(message)
        list_of_commands[index] = edited_message
    else:
        return False


def pin(message):
    if message in list_of_commands:
        list_of_commands.append(message)
        list_of_commands.remove(message)
    else:
        return False


def spam(message):
    list_of_commands.append(message)


command = input()
list_of_commands = []

while command != "end":
    current_command_list = command.split(" ")
    action = current_command_list[0]
    message = current_command_list[1]
    if action == "Chat":
        chat(message)
    elif action == "Delete":
        delete(message)
    elif action == "Edit":
        edited_message = current_command_list[2]
        edit(message)
    elif action == "Pin":
        pin(message)
    elif action == "Spam":
        for element in range(1, len(current_command_list)):
            currend_message = current_command_list[element]
            spam(currend_message)

    command = input()

if command == "end":
    print('\n'.join(list_of_commands))