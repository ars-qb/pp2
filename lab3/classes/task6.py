numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


primetest = lambda num: num>1 and all(num % i != 0 for i in range(2, num))

prime_numbers = list(filter(primetest, numbers))

print("Prime numbers:", prime_numbers)
