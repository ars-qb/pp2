def convert(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = convert(fahrenheit)
print("%i°F is equivalent to %i°C" % (fahrenheit, celsius))
