class Rectangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)


if __name__ == '__main__':
    base = 3
    height = 4
    rectangle = Rectangle(base=base, height=height)
    print(f"rectangle area {base} x {height} =", rectangle.area())

    side = 5
    square = Square(side=side)
    print(f"square area {side} x {side} =", square.area())
