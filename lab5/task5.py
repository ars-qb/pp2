import re

string = input("String: ")
pattern = r'a.*b$'

matches = re.findall(pattern, string)

print(matches)
