string = input()
command = input()
while command != "Done":
    current_command = command.split(" ")
    action = current_command[0]
    if action == "Change":
        char = current_command[1]
        replacement = current_command[2]
        string = string.replace(str(char), str(replacement), string.count(char))
        print(string)
    elif action == "Includes":
        substring = current_command[1]
        if substring in string:
            print("True")
        else:
            print("False")
    elif action == "End":
        substring = current_command[1]
        length = int(len(substring))
        if string[-length:] == substring:
            print("True")
        else:
            print("False")
    elif action == "Uppercase":
        string = string.upper()
        print(string)
    elif action == "FindIndex":
        char = current_command[1]
        index_char = string.index(char)
        print(index_char)
    elif action == "Cut":
        start_index = int(current_command[1])
        count = int(current_command[2])
        string = string[start_index:start_index+count]
        print(string)
    command = input()