print("1. Create a generator that generates the squares of numbers up to some number N")
def generator(n):
    for i in range(1, n+1):
        yield i*i

n = int(input("Input: "))
res = generator(n)
for i in range(n):
    print(next(res))


print("\n2. Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.")
def generator(n):
    for i in range(0, n+1, 2):
        yield str(i)

n = int(input("Enter a number: "))
res = generator(n)
print(",".join(res))

print("\n3. Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n")
def generator(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield str(i)
n = int(input("Enter a number: "))
res = generator(n)
print(','.join(res))



print("\nImplement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a \"for\" loop and print each of the yielded values.")
def squares(a, b):
    for i in range(a, b+1):
        yield i**2

a = int(input("A: "))
b = int(input("A: "))
res = squares(a,b)
for i in range(n):
    print(next(res))

print("\nImplement a generator that returns all numbers from (n) down to 0.")
n = int(input("Enter a number: "))
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for i in countdown(n):
    print(i)




