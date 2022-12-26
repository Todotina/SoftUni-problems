concealed_message = input()
command = input()

while command != "Reveal":
    current_command = command.split(":|:")
    action = current_command[0]
    if action == "InsertSpace":
        index = int(current_command[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif action == "Reverse":
        substring = current_command[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "")
            substring = substring[::-1]
            concealed_message = concealed_message + substring
            print(concealed_message)
        else:
            print("error")
    elif action == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]
        concealed_message = concealed_message.replace(substring, replacement, concealed_message.count(substring))
        print(concealed_message)

    command = input()

print(f"You have a new text message: {concealed_message}")