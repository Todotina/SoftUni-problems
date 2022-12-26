import re

command = input()
total_cost = 0
pattern = r'>>([A-Za-z]+)<<([0-9\.?]+)!([0-9]+)'
bought_furniture = []
while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        current_cost = float(price) * int(quantity)
        total_cost += current_cost
    command = input()
print("Bought furniture:")
for element in bought_furniture:
    print(element)
print(f"Total money spend: {total_cost:.2f}")