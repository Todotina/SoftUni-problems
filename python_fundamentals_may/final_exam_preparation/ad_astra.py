import re

string = input()
pattern = r'([\||#])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
matches = re.finditer(pattern, string)

foods = []
total_calories = 0
for match in matches:
    symbol, name, date, calories = match.groups()
    total_calories += int(calories)
    foods.append(f'Item: {name}, Best before: {date}, Nutrition: {calories}')
days = total_calories // 2000
print(f'You have food to last you for: {days} days!')
for food in foods:
    print(food)

# pattern = r'\#([A-Z][a-z]+|[A-Z][a-z]+\s[A-Z][a-z]+)\#([0-9]{2}\/[0-9]{2}\/[0-9]{2})\#(\d+)\#|\|([A-Z][a-z]+|[A-Z][a-z]+\s[A-Z][a-z]+)\|([0-9]{2}\/[0-9]{2}\/[0-9]{2})\|(\d+)\|'
# food_matches = re.findall(pattern, string)
# foods = []
# total_calories = 0
# foods_dict = {}
# for match in food_matches:
#     for element in match:
#         if len(element) > 0:
#             foods.append(element)
# for index in range(0,len(foods), 3):
#     food = foods[index]
#     date = foods[index + 1]
#     calories = int(foods[index + 2])
#     total_calories += calories
#     foods_dict[food] = {}
#     foods_dict[food]['date'] = date
#     foods_dict[food]['cal'] = calories
# days = total_calories // 2000
# print(f"You have food to last you for: {days} days!")
# for food in foods_dict:
#     print(f"Item: {food}, Best before: {foods_dict[food]['date']}, Nutrition: {foods_dict[food]['cal']}")