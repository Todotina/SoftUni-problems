number_of_days = int(input())

total_litres = 0
total_degree = 0

for days in range(number_of_days):
    current_litres = float(input())
    current_degree_per_l = float(input())
    total_litres += current_litres
    current_degree = current_degree_per_l * current_litres
    total_degree += current_degree

degrees = total_degree/total_litres
print(f"Liter: {total_litres:.2f}")
print(f"Degrees: {degrees:.2f}")

if degrees < 38:
    print("Not good, you should baking!")
elif 37 < degrees <= 42:
    print("Super!")
elif degrees > 42:
    print("Dilution with distilled water!")