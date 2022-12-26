budget = int(input())
season = input()
count_people = int(input())
price = 0
if season == "Spring":
    price = 3000
    if count_people <= 6:
        price = 0.9 * price
    elif 6 < count_people <= 11:
        price = 0.85 * price
    elif count_people > 11:
        price = 0.75 * price
elif season == "Summer" or season == "Autumn":
    price = 4200
    if count_people <= 6:
        price = 0.9 * price
    elif 6 < count_people <= 11:
        price = 0.85 * price
    elif count_people > 11:
        price = 0.75 * price
elif season == "Winter":
    price = 2600
    if count_people <= 6:
        price = 0.9 * price
    elif 6 < count_people <= 11:
        price = 0.85 * price
    elif count_people > 11:
        price = 0.75 * price
if count_people % 2 == 0 and season != "Autumn":
    price = 0.95 * price
if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")