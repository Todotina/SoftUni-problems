width = int(input())
length = int(input())
height = int(input())
command = input()
free_space = width * length * height
while command != "Done":
    current_boxes = int(command)
    free_space -= current_boxes
    if free_space <= 0:
        break
    command = input()
if command == "Done":
    print(f"{free_space} Cubic meters left.")
if free_space <= 0:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")