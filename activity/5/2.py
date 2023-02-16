from module2 import *



x = float(input("First number: "))
y = float(input("Second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == '+':
    result = add(x, y)
    print("Result:", result)
elif operation == '-':
    result = subtract(x, y)
    print("Result:", result)
elif operation == '*':
    result = multiply(x, y)
    print("Result:", result)
elif operation == '/':
    result = divide(x, y)
    print("Result:", result)
else:
    print("Invalid operation")
