import os

path = input("Enter a path: ")

if os.path.exists(path):
    print("Exists")

    directory, filename = os.path.split(path)

    print(f"Directory: %s" % directory)
    print(f"Filename: %s" % filename)
else:
    print("Not exist")
