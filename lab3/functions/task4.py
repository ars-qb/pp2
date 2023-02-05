

def filter_primes(numbers):
    primetest = lambda num: num > 1 and all(num % i != 0 for i in range(2, num))

    return list(filter(primetest, numbers))

inp = input("Numbers: ")
numbers = list(map(int, inp.split()))
prime_numbers = filter_primes(numbers)

print("Prime numbers:", prime_numbers)
