import re

camel_case_string = input("String: ")
pattern = r'(?<!^)(?=[A-Z])'
snake_case_string = re.sub(pattern, lambda x: '_' + x.group(0).lower(), camel_case_string)

print(snake_case_string)
