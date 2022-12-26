vacation_days = int(input())
accommodation_type = input()
score = input()

number_of_nights = vacation_days - 1
price_per_night = 0
discount = 0

if accommodation_type == "room for one person":
    price_per_night = 18
elif accommodation_type == "apartment":
    price_per_night = 25
    if vacation_days < 10:
        discount = 0.3
    elif vacation_days <= 15:
        discount = 0.35
    elif vacation_days > 15:
        discount = 0.5
elif accommodation_type == "president apartment":
    price_per_night = 35
    if vacation_days < 10:
        discount = 0.1
    elif vacation_days <= 15:
        discount = 0.15
    elif vacation_days > 15:
        discount = 0.2

total_price = (number_of_nights * price_per_night) * (1 - discount)
if score == "positive":
    total_price *= 1.25
elif score == "negative":
    total_price *= 0.9
print(f"{total_price:.2f}")