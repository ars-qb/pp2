def f(word):
    res=0
    vowels = ["a","e", "i", "o", "u"]
    for i in word:
        if i in vowels:
            res+=1

    return res

def main():
    print(f(input("Word: ")))

if __name__ == '__main__':
    main()