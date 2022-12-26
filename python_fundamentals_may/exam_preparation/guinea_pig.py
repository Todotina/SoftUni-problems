food_kg = float(input())
hay_kg = float(input())
cover_kg = float(input())
weight = float(input())
days_count = 0
while food_kg > 0 and hay_kg > 0 and cover_kg > 0:
    for day in range(1, 30 + 1):
        days_count += 1
        food_kg -= 0.3
        if day % 2 == 0:
            hay_kg -= 0.05 * food_kg
        if day % 3 == 0:
            cover_kg -= 0.33333 * weight
        if food_kg <= 0 or hay_kg <= 0 or cover_kg <= 0:
            print("Merry must go to the pet store!")
            break
    if days_count == 30:
        print(f"Everything is fine! Puppy is happy! Food: {food_kg:.2f}, Hay: {hay_kg:.2f}, Cover: {cover_kg:.2f}.")
        break



