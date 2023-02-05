def permutations(data, index=0):
    if index == len(data) - 1:
        print(''.join(data))
    else:
        for i in range(index, len(data)):
            data[index], data[i] = data[i], data[index]
            permutations(data, index + 1)
            data[index], data[i] = data[i], data[index]

inp = input("String: ")
permutations(list(inp))
