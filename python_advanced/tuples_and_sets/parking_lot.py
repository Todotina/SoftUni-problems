commands = int(input())
cars = set()
for car in range(commands):
    current_car = input().split(", ")
    direction, plate = current_car[0], current_car[1]
    if direction == "IN":
        cars.add(plate)
    elif direction == "OUT":
        cars.remove(plate)
if len(cars) > 0:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")