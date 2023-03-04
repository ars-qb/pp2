def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s.lower()))
    return s == s[::-1]

s = input("Enter a string: ")

if is_palindrome(s):
    print("%s is a palindrome." % s)
else:
    print("%s is not a palindrome." % s)
