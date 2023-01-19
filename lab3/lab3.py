### Python Functions

#1
def my_function():
  print("Hello from a function")

#2
def my_function():
  print("Hello from a function")

my_function()

# 3
def my_function(fname, lname):
  print(fname)

# 4
def my_function(x):
    return x+5

# 5
def my_function(*kids):
  print("The youngest child is " + kids[2])

# 6
def my_function(**kid):
  print("His last name is " + kid["lname"])

### Python Lamda

# 1
x = lambda a: a

### Python Classes
# 1
class MyClass:
  x = 5
# 2
class MyClass:
  x = 5

p1 = MyClass()

# 3

class MyClass:
  x = 5

p1 = MyClass()

print(p1.x)

# 4
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

### Python Inheritance
#1
class Student(Person):

# 2
class Person:
    def __init__(self, fname):
        self.firstname = fname

    def printname(self):
        print(self.firstname)

class Student(Person):
    pass

x = Student("Mike")

x.printname()

### Python Modules

# 1
import mymodule

# 2
import mymodule as mx

# 3
import mymodule
print(dir(mymodule))

#4
from mymodule import person1


