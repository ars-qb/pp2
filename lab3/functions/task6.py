def reverse(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

inp = input("Sentence: ")
print(reverse(inp))
