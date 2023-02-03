
class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters


    def print(self):
        print(self.letters)

    def letters_num(self):
        print(len(self.letters))



class EngAlphabet(Alphabet):
    _letters_num = 26

    def __init__(self, lang, letters):
        super().__init__(lang, letters)


    def is_en_letter(self, letter):
        print(letter in self.letters + self.letters.upper())

    def letters_num(self):
        print(EngAlphabet._letters_num)

    @staticmethod
    def example():
        print("This is Example Text in Englishhhhhhhh")


ru = Alphabet("RU", "абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
ru.print()
ru.letters_num()


en = EngAlphabet("EN", "abcdefghijklmnopqrstuvwxyz")
en.print()
en.letters_num()
en.is_en_letter("a")
en.example()