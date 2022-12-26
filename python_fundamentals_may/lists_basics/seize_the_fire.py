def range_of_fire_is_valid(type, range):
    if type == "High":
        if 81 <= range <= 125:
            return True
    elif type == "Medium":
        if 51 <= range <= 80:
            return True
    elif type == "Low":
        if 1 <= range <= 50:
            return True
    else:
        return False


fires_and_cells = input().split("#")
cells_list = []
water = int(input())
total_effort =0
total_fire = 0

for element in fires_and_cells:
    current_fire = element.split(" = ")
    type_of_fire = current_fire[0]
    value = int(current_fire[1])
    if range_of_fire_is_valid(type_of_fire, value):
        if water >= value:
            cells_list.append(value)
            water -= value
            effort = 0.25 * value
            total_effort += effort
            total_fire += value
        else:
            continue

print("Cells:")
for cell in cells_list:
    print("- " + str(cell))
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")