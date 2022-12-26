from math import pi
figure = input()
if figure == "square":
    side = float(input())
    print(f"{side * side:.3f}")
elif figure == "rectangle":
    side1 = float(input())
    side2 = float(input())
    print(f"{side1 * side2:.3f}")
elif figure == "circle":
    radius = float(input())
    print(f"{radius **2 * pi:.3f}")
elif figure == "triangle":
    side1 = float(input())
    height = float(input())
    print(f"{side1 * height/2:.3f}")