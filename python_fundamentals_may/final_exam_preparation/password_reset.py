def password_reset():
    data = input()

    while True:
        command = input().split(' ')
        current_command = command[0]

        if current_command == 'Done':
            print(f'Your password is: {data}')
            break

        elif current_command == 'TakeOdd':
            data = ''.join([data[i] for i in range(len(data)) if i % 2 != 0])
            print(data)

        elif current_command == 'Cut':
            index = int(command[1])
            length = int(command[2])
            data = ''.join([data[i] for i in range(len(data)) if i < index or i >= index + length])
            print(data)

        elif current_command == 'Substitute':
            substring = command[1]
            substitute = command[2]

            if substring in data:
                data = data.replace(substring, substitute)
                print(data)
            else:
                print("Nothing to replace!")


password_reset()

# def take_odd(string):
#     password = ''
#     for i in range(len(string)):
#         if i % 2 != 0:
#             password += string[i]
#     print(password)
#     list_with_passwords.append(password)
#
#
# def cut(string):
#     string_to_be_cut = string[index:index + length]
#     string = string.replace(string_to_be_cut, '')
#     print(string)
#     list_with_passwords.append(string)
#
#
# def substitute_string(string, substring, substitute):
#     if substring in string:
#         string = string.replace(substring, substitute, string.count(substring))
#         print(string)
#         list_with_passwords.append(string)
#     else:
#         print("Nothing to replace!")
#
#
# string = input()
# list_with_passwords = []
# command = input()
# while command != "Done":
#     current_command = command.split(' ')
#     action = current_command[0]
#     if action == "TakeOdd":
#         take_odd(string)
#     elif action == "Cut":
#         index = int(current_command[1])
#         length = int(current_command[2])
#         cut(list_with_passwords[-1])
#     elif action == "Substitute":
#         substring = current_command[1]
#         substitute = current_command[2]
#         substitute_string(list_with_passwords[-1], substring, substitute)
#
#     command = input()
#
# print(f"Your password is: {list_with_passwords[-1]}")