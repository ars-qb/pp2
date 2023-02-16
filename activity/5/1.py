x = input("Enter the number of Fibonacci terms to generate: ")
x = int(x)

def Fibonacci(x):
    l=[0,1]
    for i in range(1,x-1):
        l.append(l[i-1]+l[i])

    yield l

print(*Fibonacci(x))


