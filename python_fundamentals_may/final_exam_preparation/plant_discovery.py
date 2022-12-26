number = int(input())
plants = {}
for number in range(number):
    current_plant = input().split("<->")
    plant = current_plant[0]
    rarity = int(current_plant[1])
    if plant not in plants:
        plants[plant] = {}
        plants[plant]["Rarity"] = int(rarity)
        plants[plant]["Rating"] = []

command = input()

while command != "Exhibition":
    current_command = command.split(": ")
    action = current_command[0]
    last_command = current_command[1].split(" - ")
    plant = last_command[0]
    if action == "Rate":
        if plant not in plants:
            print("error")
        else:
            rating = int(last_command[1])
            plants[plant]["Rating"].append(rating)
    elif action == "Update":
        if plant not in plants:
            print("error")
        else:
            new_rarity = int(last_command[1])
            plants[plant]["Rarity"] = new_rarity
    elif action == "Reset":
        if plant not in plants:
            print("error")
        else:
            plants[plant]["Rating"].clear()

    command = input()

print("Plants for the exhibition:")
for plant in plants:
    if len(plants[plant]["Rating"]) > 0:
        average_rating = sum(plants[plant]["Rating"]) / int(len(plants[plant]["Rating"]))
        plants[plant]["Rating"] = average_rating
    else:
        average_rating = 0
        plants[plant]["Rating"] = 0
    rarity = plants[plant]["Rarity"]
    print(f'- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}')

