import re

username = input("Username: ")
password = input("Password: ")
email = input("Email: ")

x=re.match(r"^[a-zA-Z][a-zA-Z0-9_]{4,19}$", username)
y=re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", password)
z=re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)

if x and y and z:
    print("Registration was successful")
else:
    print("Registration was fail")

