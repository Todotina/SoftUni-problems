command = input()
towns = {}
while command != "Sail":
    current_town = command.split("||")
    town, people, gold = current_town[0], int(current_town[1]), int(current_town[2])
    if town not in towns:
        towns[town] = {}
        towns[town]['people'] = people
        towns[town]['gold'] = gold
    else:
        towns[town]['people'] += people
        towns[town]['gold'] += gold
    command = input()


def plunder_town(town, people, gold):
    if towns[town]['people'] >= people and towns[town]['gold'] >= gold:
        towns[town]['people'] -= people
        towns[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if towns[town]['people'] <= 0 or towns[town]['gold'] <= 0:
        print(f"{town} has been wiped off the map!")
        del towns[town]


def prosper_town(town, gold):
    if gold >= 0:
        towns[town]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {towns[town]['gold']} gold.")
    else:
        print("Gold added cannot be a negative number!")


event = input()
while event != "End":
    current_event = event.split("=>")
    action, town = current_event[0], current_event[1]
    if action == "Plunder":
        people, gold = int(current_event[2]), int(current_event[3])
        plunder_town(town, people, gold)
    elif action == "Prosper":
        gold = int(current_event[2])
        prosper_town(town, gold)

    event = input()

if len(towns) > 0:
    print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
    for town in towns:
        print(f"{town} -> Population: {towns[town]['people']} citizens, Gold: {towns[town]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")