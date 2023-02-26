import re

string = input("String: ")
pattern = r'[ ,.]'

res = re.sub(pattern, ':', string)

print(res)
