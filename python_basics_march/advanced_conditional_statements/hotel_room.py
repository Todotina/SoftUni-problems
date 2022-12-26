month = input()
number_of_nights = int(input())

price_per_night_studio = 0
price_per_night_apartment = 0

if month == "May" or month == "October":
    price_per_night_studio = 50
    price_per_night_apartment = 65
    if 7 < number_of_nights <= 14:
        price_per_night_studio = 0.95 * price_per_night_studio
    elif number_of_nights > 14:
        price_per_night_studio = 0.7 * price_per_night_studio
        price_per_night_apartment = 0.9 * price_per_night_apartment
elif month == "June" or month == "September":
    price_per_night_studio = 75.20
    price_per_night_apartment = 68.70
    if number_of_nights > 14:
        price_per_night_studio = 0.8 * price_per_night_studio
        price_per_night_apartment = 0.9 * price_per_night_apartment
elif month == "July" or month == "August":
    price_per_night_studio = 76
    price_per_night_apartment = 77
    if number_of_nights > 14:
        price_per_night_apartment = 0.9 * price_per_night_apartment

print(f"Apartment: {number_of_nights * price_per_night_apartment:.2f} lv.")
print(f"Studio: {number_of_nights * price_per_night_studio:.2f} lv.")