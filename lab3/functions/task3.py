def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return (chickens, rabbits)

    return None, None


numheads = 17
numlegs = 64

chickens, rabbits = solve(numheads, numlegs)

if chickens:
    print("%i chickens\n%i rabbits" % (chickens, rabbits))
else:
    print("Can't found")

