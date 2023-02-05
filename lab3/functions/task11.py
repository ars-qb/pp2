def is_palindrome(string):
    string = string.lower()
    string = string.replace(" ", "")
    return string == string[::-1]

string = input("String: ")
print(is_palindrome(string))


