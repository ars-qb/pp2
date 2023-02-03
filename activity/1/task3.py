data = {}
def f(word):
    for i in word:
        if i in data:
            data[i]+=1
        else:
            data.setdefault(i, 1)

    return data


def main():
    res = f(input("Word: "))

    for k,v in res.items():

        print('%s -> %i' % (k,v))

if __name__ == '__main__':
    main()