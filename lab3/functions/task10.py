def unique(lst):
    res = []
    for elem in lst:
        if not elem in res:
            res.append(elem)
    return res

input_list = [100, 100, 100, 1, 1, 9,10]
print(unique(input_list))
