def sphere_volume(radius):
    return 4/3 * 3.14 * (radius ** 3)

radius = int(input("Sphere's radius: "))
volume = sphere_volume(radius)
print("The volume is %.2f" % volume)
