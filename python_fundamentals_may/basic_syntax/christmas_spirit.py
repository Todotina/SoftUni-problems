quantity_decorations = int(input())
days_left = int(input())
price_ornament = 2
price_skirt = 5
price_garland = 3
price_lights = 15
quantity_ornament = 0
quantity_skirt = 0
quantity_garland = 0
quantity_lights = 0
spirit = 0
for day in range(1, days_left + 1):
    if day % 11 ==0:
        quantity_decorations += 2
    if day % 2 == 0:
        quantity_ornament += 1
        spirit += 5
    if day % 3 == 0:
        quantity_skirt += 1
        quantity_garland += 1
        spirit += 13
    if day % 5 == 0:
        quantity_lights += 1
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        quantity_skirt = 1
        quantity_lights = 1
        quantity_garland = 1
        quantity_ornament = 0
if days_left % 10 == 0:
    spirit -= 30
cost = quantity_decorations * (quantity_garland * price_garland + quantity_ornament * price_ornament + quantity_skirt * price_skirt + quantity_lights * price_lights)
print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")