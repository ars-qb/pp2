num = int(input("Num: "))

def Work(num):
    sign = 1 if num >= 0 else -1
    num *= sign
    res = 0
    while num > 0:
        res = res * 10 + num % 10
        num = num // 10

    return sign * res

print(Work(num))