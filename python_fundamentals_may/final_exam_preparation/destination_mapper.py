import re

pattern = r'=[A-Z][a-zA-Z][a-zA-Z]+=|\/[A-Z][a-zA-Z][a-zA-Z]+\/'
locations = input()
valid_locations = re.findall(pattern, locations)
travel_points = 0
destinations = []
for location in valid_locations:
    destination = location[1:-1]
    destinations.append(destination)
for i in destinations:
    travel_points += int(len(i))
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")