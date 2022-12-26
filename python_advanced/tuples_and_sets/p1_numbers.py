line_one = set(input().split())
line_two = set(input().split())
number_of_commands = int(input())

for command in range(number_of_commands):
    current_command = input().split()
    action, line = current_command[0], current_command[1]
    if action == "Add":
        if line == "First":
            for item in range(2, len(current_command)):
                line_one.add(item)
        elif line == "Second":
            for item in range(2, len(current_command)):
                line_two.add(int(item))
    elif action == "Remove":
        if line == "First":
            for item in range(2, len(current_command)):
                if item in line_one:
                    line_one.remove(item)
        elif line == "Second":
            for item in range(2, len(current_command)):
                if item in line_two:
                    line_two.remove(item)
    elif action == "Check":
        if line_one < line_two or line_two < line_one:
            print("True")
        else:
            print("False")
print(', '.join(str(sorted(map(int, line_one)))))
print(', '.join(str(sorted(map(int, line_two)))))