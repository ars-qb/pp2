x = int(input("X: "))
y = int(input("Z: "))
op = input("Operation: ")

if op == "+":
    r = lambda x,y: x+y
    print(r(x,y))
elif op == "-":
    r = lambda x, y: x - y
    print(r(x, y))
elif op == "*":
    r = lambda x, y: x * y
    print(r(x, y))
elif op == "/":
    r = lambda x, y: x / y
    print(r(x, y))
else:
    raise Warning("Enter +,-,*,/ operation")

