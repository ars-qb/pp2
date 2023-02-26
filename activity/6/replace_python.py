import re

sentence = input("Enter a sentence containing the word \"Python\": ")
result = re.sub("Python", "Java", sentence)
print(result)