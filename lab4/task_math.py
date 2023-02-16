import math
print("1. Write a Python program to convert degree to radian.")
x=float(input("Input degree: "))
print("Output radian: ", math.radians(x))


print("\n2. Write a Python program to calculate the area of a trapezoid.")
h= float(input("Height: "))
b1 = float(input("Base, first value: "))
b2 = float(input("Base, second value: "))
print("Expected Output: ", (b1+b2)*0.5*h)

print("\n3. Write a Python program to calculate the area of regular polygon.")
n= int(input("Input number of sides: "))
l= float(input("Input the length of a side: "))
area = (n * l ** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is: ", area)

print("\nWrite a Python program to calculate the area of a parallelogram.")
l= float(input("Length of base: "))
h = float(input("Height of parallelogram: "))
print("Expected Output: ", l*h)