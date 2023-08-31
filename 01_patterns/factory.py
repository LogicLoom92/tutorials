class Shape:
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        return "Drawing a circle"


class Square(Shape):
    def draw(self):
        return "Drawing a square"


class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()


# Usage
factory = ShapeFactory()
circle = factory.create_shape("circle")
square = factory.create_shape("square")

print(circle.draw())
print(square.draw())
