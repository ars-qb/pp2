import os

path = input("Enter path: ")
ext = input("Enter extension: ")

for file in os.listdir(path):
    if file.endswith(ext):
        print(file)