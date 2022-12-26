number_of_floors = int(input())
number_of_rooms = int(input())
space = ""
for floors in range(number_of_floors, 0, -1):
    for rooms in range(number_of_rooms):
        if floors == number_of_floors:
            space = "L"
        elif floors % 2 != 0:
            space = "A"
        else:
            space = "O"
        print(f" {space}{floors}{rooms}", end = "")
    print()