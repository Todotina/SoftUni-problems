command = input()
length = 0
while command != "Welcome!":
    if command == "Voldemort":
        print("You must not speak of that name!")
        break
    length = len(command)
    if length < 5:
        print(f"{command} goes to Gryffindor.")
    elif length == 5:
        print(f"{command} goes to Slytherin.")
    elif length == 6:
        print(f"{command} goes to Ravenclaw.")
    else:
        print(f"{command} goes to Hufflepuff.")
    command = input()
if command == "Welcome!":
    print("Welcome to Hogwarts.")