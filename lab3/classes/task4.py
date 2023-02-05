
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print('(%i, %i)' % (self.x, self.y))

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def dist(self, second_x, second_y):
        return ((self.x - second_x) ** 2 + (self.y - second_y) ** 2) ** 0.5


x = int(input("x: "))
y = int(input("y: "))

point = Point(x,y)
point.show()

delta_x = int(input("Delta x: "))
delta_y = int(input("Delta y: "))
point.move(x,y)
point.show()

second_x = int(input("Second x: "))
second_y = int(input("Second y: "))

print(point.dist(second_x, second_y))




