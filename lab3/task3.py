class W:
    def __init__(self, array):
        self.array = array

    def unique(self):
        _unique = []
        for element in self.array:
            if self.array.count(element) == 1:
                _unique.append(element)
        return _unique

    def repeated(self):
        _repeated = []

        for element in set(self.array):
            if self.array.count(element) > 1:
                _repeated.append((element, self.array.count(element)))
        return _repeated



a = ["Almaty", 12, 3, 4, 4, 5, 5, 5, 12, "1", 7, 1, "Alma", "A", "B", "Alma", 12]

c = W(a)


print("Unique elements:")
print(', '.join(str(i) for i in c.unique()))
print("\n")
print("Repeated elements:")
print('\n'.join('%s -> %s' % i for i in c.repeated()))