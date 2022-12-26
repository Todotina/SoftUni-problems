number = int(input())
registered_cars = {}
for command in range(number):
    current_command = input().split(" ")
    action, name = current_command[0], current_command[1]
    if len(current_command) == 3:
        plate = current_command[2]
        if name not in registered_cars:
            registered_cars[name] = 0
            registered_cars[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    else:
        if name in registered_cars:
            print(f"{name} unregistered successfully")
            del registered_cars[name]
        else:
            print(f"ERROR: user {name} not found")

for name, plate in registered_cars.items():
    print(f"{name} => {plate}")