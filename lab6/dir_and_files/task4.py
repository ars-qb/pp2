filename = input("Enter the filename: ")

with open(filename, 'r') as file:
    line_count = 0
    for line in file:
        line_count += 1

print(f"The file %s has %i lines" % (filename, line_count))
