message = input()
command = input()

while command != "Decode":
    instruction = command.split('|')
    action = instruction[0]
    if action == "Move":
        number_of_letters = int(instruction[1])
        message = message[number_of_letters:] + message[:number_of_letters]
    elif action == "Insert":
        index, value = int(instruction[1]), instruction[2]
        message = message[:index] + value + message[index:]
    elif action == "ChangeAll":
        substring, replacement = instruction[1], instruction[2]
        message = message.replace(substring, replacement, message.count(substring))

    command = input()

print(f"The decrypted message is: {message}")