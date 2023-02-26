import re
string = input("String: ")

pattern = r'[A-Z][a-z]+'

matches = re.findall(pattern, string)

print(matches)
