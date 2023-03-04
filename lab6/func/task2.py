# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

def count_upper_lower(s):
    upper_count = 0
    lower_count = 0
    for c in s:
        if c.isupper():
            upper_count += 1
        elif c.islower():
            lower_count += 1
    return upper_count, lower_count


inp = input("Enter string: ")
upper_count, lower_count = count_upper_lower(inp)
print(f"Number of uppercase letters: %s" % upper_count)
print(f"Number of lowercase letters: %s" % lower_count)
