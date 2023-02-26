import re

phone = input("Enter number: ")
# XXX-XXX-XXXX
pattern = r"^[0-9]{3}-[0-9]{3}-[0-9]{4}$"

x=re.match(pattern, phone)
if x:
    print("Valid")
else:
    print("Invalid")