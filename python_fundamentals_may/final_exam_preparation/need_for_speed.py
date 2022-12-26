number_of_cars = int(input())
cars = {}

for i in range(number_of_cars):
    current_car = input().split("|")
    car, mileage, fuel = current_car[0], int(current_car[1]), int(current_car[2])
    if car not in cars:
        cars[car] = {}
        cars[car]['mileage'] = mileage
        cars[car]['fuel'] = fuel


def drive_distance(car, distance, fuel):
    if cars[car]['fuel'] >= fuel:
        cars[car]['fuel'] -= fuel
        cars[car]['mileage'] += distance
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]['mileage'] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]
    else:
        print("Not enough fuel to make that ride")


def refill_tank(car, fuel):
    difference = 75 - cars[car]['fuel']
    if fuel > difference:
        cars[car]['fuel'] += difference
        print(f"{car} refueled with {difference} liters")
    else:
        cars[car]['fuel'] += fuel
        print(f"{car} refueled with {fuel} liters")


def revert_kilometers(car, kilometers):
    cars[car]['mileage'] -= kilometers
    print(f"{car} mileage decreased by {kilometers} kilometers")
    if cars[car]['mileage'] < 10000:
        cars[car]['mileage'] = 10000


command = input()
while command != "Stop":
    current_command = command.split(" : ")
    action, car = current_command[0], current_command[1]
    if action == "Drive":
        distance, fuel = int(current_command[2]), int(current_command[3])
        drive_distance(car, distance, fuel)
    elif action == "Refuel":
        fuel = int(current_command[2])
        refill_tank(car, fuel)
    elif action == "Revert":
        kilometers = int(current_command[2])
        revert_kilometers(car, kilometers)

    command = input()

for car in cars:
    print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")