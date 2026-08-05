# Base Class
class Shape:
    def __init__(self):
        print("Shape Created")


# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Main Program
circle = Circle(5)
rectangle = Rectangle(10, 6)

print("Area of Circle:", circle.area())
print("Area of Rectangle:", rectangle.area())