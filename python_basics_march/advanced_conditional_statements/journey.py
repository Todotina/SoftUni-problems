budget = float(input())
season = input()
destination = ""
trip_value = 0
accommodation = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        trip_value = 0.3 * budget
        accommodation = "Camp"
    elif season == "winter":
        trip_value = 0.7 * budget
        accommodation = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        trip_value = 0.4 * budget
        accommodation = "Camp"
    elif season == "winter":
        trip_value = 0.8 * budget
        accommodation = "Hotel"
elif budget > 1000:
    destination = "Europe"
    trip_value = 0.9 * budget
    accommodation = "Hotel"
print(f"Somewhere in {destination}")
print(f"{accommodation} - {trip_value:.2f}")
