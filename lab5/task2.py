import re

string = input("String: ")

pattern = r'a[b]{2,3}'
matches = re.findall(pattern, string)
print(matches)
