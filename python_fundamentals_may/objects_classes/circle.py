class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self, __pi=3.14):
        return self.diameter * Circle.__pi

    def calculate_area(self, __pi=3.14):
        return Circle.__pi * (self.radius ** 2)

    def calculate_area_of_sector(self, angle):
        return Circle.__pi * (angle/360) * self.radius ** 2

circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")