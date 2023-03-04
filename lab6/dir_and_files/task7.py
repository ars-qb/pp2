
file1 = input("Source file: ")
file2 = input("Destination file: ")

with open(file1, 'r') as f:
    contents = f.read()

with open(file2, 'w') as f:
    f.write(contents)