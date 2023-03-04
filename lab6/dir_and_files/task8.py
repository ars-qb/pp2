import os

filepath = input("File: ")

if not os.path.exists(filepath):
    print(f"Error: File %s does not exist" % filepath)
    exit()

if not os.access(filepath, os.W_OK):
    print(f"Error: Permission denied to delete file %s" % filepath)
    exit()
os.remove(filepath)


