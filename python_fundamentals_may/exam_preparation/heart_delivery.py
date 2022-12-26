list_with_integers = [int(number) for number in input().split("@")]
command = input()
needed_hearts = 0
while command != "Love!":
    current_command_list = command.split(" ")
    length = int(current_command_list[1])
