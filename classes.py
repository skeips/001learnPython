import math
class Circle:
    is_shape = True

    def __init__(self, radius, color='red'):
        self.radius = radius
        self.color = color

    def area(self):
        return math.pi * self.radius ** 2
    

circle = Circle(3)
circle.area()

print(circle.area())