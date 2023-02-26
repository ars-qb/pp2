import re
string = input("String: ")
pattern = r'(?<!^)(?=[A-Z])'
new_string = re.sub(pattern, ' ', string)
print(new_string)
