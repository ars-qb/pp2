import re

snake_case_string = input("String: ")

pattern = r'_([a-z])'

camel_case_string = re.sub(pattern, lambda x: x.group(1).upper(), snake_case_string)

camel_case_string = camel_case_string[0].upper() + camel_case_string[1:]

print(camel_case_string)
