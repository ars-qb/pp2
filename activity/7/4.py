name = input("Enter name of file: ")
word = input("Enter word: ")

with open(name, "r") as f:
    content = f.read().lower()

print(content.count(word.lower()))