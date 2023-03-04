list_of_strings = ['Nodejs', 'Almaty', 'KBTU', 'New York', 'Astana', 'Python']
filename = input("Enter the filename: ")

with open(filename, 'w') as file:
    for string in list_of_strings:
        file.write(f"{string}\n")

print(f"The list has been written to the file %s" % filename)
