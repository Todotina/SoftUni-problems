days = int(input())
accommodation = input()
review = input()
price_room = 18
price_apartment = 25
price_president = 35

nights = abs(days - 1)

if accommodation == "room for one person":
    value = price_room * nights
elif accommodation == "apartment":
    value = price_apartment * nights
    if days < 10:
        value = 0.7 * value
    elif 10 <= days <= 15:
        value = 0.65 * value
    elif days > 15:
        value = 0.5 * value
elif accommodation == "president apartment":
    value = price_president * nights
    if days < 10:
        value = 0.9 * value
    elif 10 <= days <= 15:
        value = 0.85 * value
    elif days > 15:
        value = 0.8 * value
final_price = value
if review == "positive":
    final_price = 1.25 * value
elif review == "negative":
    final_price = 0.9 * value

print(f"{final_price:.2f}")