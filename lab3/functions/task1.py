
def convert(grams):
    return 28.3495231 * grams

grams = float(input("Enter the weight in grams: "))
ounces = convert(grams)
print("%i grams is equal to %i ounces." % (grams, ounces))

