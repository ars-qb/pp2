class IOString:
    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())


IO = IOString()
IO.getString()
IO.printString()



