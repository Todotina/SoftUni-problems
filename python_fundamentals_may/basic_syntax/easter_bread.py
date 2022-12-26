budget = float(input())
price_kg_flour = float(input())
price_pack_eggs = 0.75 * price_kg_flour
price_l_milk = 1.25 * price_kg_flour
price_250ml_milk = price_l_milk / 4
price_per_loaf = price_250ml_milk + price_pack_eggs + price_kg_flour
number_of_loaves = int(budget // price_per_loaf)
budget_left = budget - (number_of_loaves * price_per_loaf)
number_of_eggs = 0
eggs_lost = 0
total_eggs_lost = 0
for loaf in range(1, number_of_loaves + 1):
    number_of_eggs += 3
    if loaf % 3 == 0:
        eggs_lost = loaf - 2
        total_eggs_lost += eggs_lost
total_number_eggs = int(number_of_eggs - total_eggs_lost)
print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {total_number_eggs} eggs and {budget_left:.2f}BGN left.")