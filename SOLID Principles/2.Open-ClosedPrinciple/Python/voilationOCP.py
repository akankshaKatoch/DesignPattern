# This code violates the Open-Closed Principle (OCP) because
# the AreaCalculator class must be modified every time a new shape is added.

class AreaCalculator:
    def calculate_area(self, shape):
        # Check if the shape is a Rectangle
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        # Check if the shape is a Circle
        elif isinstance(shape, Circle):
            return 3.14 * shape.radius * shape.radius
        # If a new shape is added, this method must be modified
        else:
            return None

class Rectangle:
    def __init__(self, width, height):
        # Initialize width and height for Rectangle
        self.width = width
        self.height = height

class Circle:
    def __init__(self, radius):
        # Initialize radius for Circle
        self.radius = radius

# Usage example
shapes = [Rectangle(10, 20), Circle(5)]
calculator = AreaCalculator()
for shape in shapes:
    print(calculator.calculate_area(shape))