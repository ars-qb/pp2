class Shape:
    def __init__(self):
        self.area = 0

    def area(self):
        print(self.area)

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length ** 2)


IO = Square(100)

IO.area()

