import math

days_away = int(input())
left_food_kg = int(input())
deer_one_daily_food_kg = float(input())
deer_two_daily_food_kg = float(input())
deer_three_daily_food_kg = float(input())
needed_food = days_away * (deer_one_daily_food_kg + deer_two_daily_food_kg + deer_three_daily_food_kg)
delta = abs(needed_food - left_food_kg)
if left_food_kg >= needed_food:
    print(f"{math.floor(delta)} kilos of food left.")
else:
    print(f"{math.ceil(delta)} more kilos of food are needed.")