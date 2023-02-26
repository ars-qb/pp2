import re


string = input("String: ")
pattern = r'[a-z]+_[a-z]+'
matches = re.findall(pattern, string)
print(matches)
