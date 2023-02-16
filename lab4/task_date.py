from datetime import *


print("1. Write a Python program to subtract five days from current date")

today = datetime.today()
result = today - timedelta(days=5)
print(result)

print("\n2. Write a Python program to print yesterday, today, tomorrow.")
print("Yesterday:", datetime.today()-timedelta(days=1))
print("Today:", datetime.today())
print("Tomorrow:", datetime.today()+timedelta(days=1))

print("\n3. Write a Python program to drop microseconds from datetime.")

print(datetime.now().replace(microsecond=0))

print("\n4. Write a Python program to calculate two date difference in seconds.")
import datetime


date1 = datetime.datetime(2004, 2, 16, 12, 0, 0)
date2 = datetime.datetime(2023, 2, 16, 14, 30, 0)

delta_seconds = (date2 - date1).total_seconds()

print("The difference between the two dates is", delta_seconds, "seconds.")

