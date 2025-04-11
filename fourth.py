import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
   
    def area(self):
        return math.pi * self.radius ** 2
   
    def circumference(self):
        return 2 * math.pi * self.radius

circle = Circle(5)
print(f"Площадь окружности: {circle.area()}")
print(f"Длина окружности: {circle.circumference()}")

