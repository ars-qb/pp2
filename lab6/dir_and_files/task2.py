import os

path = input("Enter the path: ")

if os.path.exists(path):
    print("Not exist")
    if os.access(path, os.R_OK):
        print("Readable")
    else:
        print("Not readable")

    if os.access(path, os.W_OK):
        print("Writable")
    else:
        print("Not writable")

    if os.access(path, os.X_OK):
        print("Executable")
    else:
        print("Not executable")

else:
    print("Exists")


