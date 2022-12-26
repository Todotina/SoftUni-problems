flower_type = input()
number_of_flowers = int(input())
budget = int(input())
price = 0
value = 0
if flower_type == "Roses":
    price = 5
    value = number_of_flowers * price
    if number_of_flowers > 80:
        value = 0.9 * number_of_flowers * price
elif flower_type == "Dahlias":
    price = 3.80
    value = number_of_flowers * price
    if number_of_flowers > 90:
        value = 0.85 * number_of_flowers * price
elif flower_type == "Tulips":
    price = 2.80
    value = number_of_flowers * price
    if number_of_flowers > 80:
        value = 0.85 * number_of_flowers * price
elif flower_type == "Narcissus":
    price = 3
    value = number_of_flowers * price
    if number_of_flowers < 120:
        value = 1.15 * number_of_flowers * price
elif flower_type == "Gladiolus":
    price = 2.50
    value = number_of_flowers * price
    if number_of_flowers < 80:
        value = 1.2 * number_of_flowers * price

if budget >= value:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower_type} and {budget - value:.2f} leva left.")
else:
    print(f"Not enough money, you need {value - budget:.2f} leva more.")
