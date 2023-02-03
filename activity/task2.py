def f(word):
    if len(word) %2 == 0:

        while word:
            if word[0] == word[-1]:
                word = word[1:]
                word = word[:-1]
            else: return False
    else:
        while len(word)!=1:
            if word[0] == word[-1]:
                word = word[1:]
                word = word[:-1]
            else: return False


    return True

def main():
    print(f(input("Word: ")))

if __name__ == '__main__':
    main()