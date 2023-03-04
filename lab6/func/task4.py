# Write a Python program that invoke square root function after specific milliseconds. Sample Input: 25100 2123 Sample Output: Square root of 25100 after 2123 miliseconds is 158.42979517754858
import time
import math

num = int(input("Enter a number: "))
milliseconds = int(input("Enter the number of milliseconds: "))

time.sleep(milliseconds / 1000)
result = math.sqrt(num)

print("Square root of %i after %i milliseconds is %f" % (num, milliseconds, result))
