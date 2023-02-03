class TriangleChecker:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def is_triangle(self):
        x = self.x
        y = self.y
        z = self.z

        try:
            x = int(x)
            y = int(y)
            z = int(z)
        except:
            return "You only need to enter numbers!"

        if x<0 or y<0 or z<0:
            return "Nothing will work with negative numbers!"
        elif x+y>z and y+z>x and x+z>y:
            return "You can build a triangle!"
        else:
            return "It's a pity, but you can't make a triangle out of this."


x = input("X: ")
y = input("Y: ")
z = input("Z: ")
Checker = TriangleChecker(x,y,z)
print(Checker.is_triangle())