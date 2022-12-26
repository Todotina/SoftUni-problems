count_cakes = int(input())
count_egg_cartons = int(input())
kilos_cookies = int(input())
sum_cakes = count_cakes * 3.20
sum_eggs = count_egg_cartons * 4.35
sum_cookies = kilos_cookies * 5.40
sum_paint = count_egg_cartons * 12 * 0.15
total_amount = sum_paint + sum_cookies + sum_eggs + sum_cakes
print(f"{total_amount:.2f}")