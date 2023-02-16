import json

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


    def to_json(self):

        return self.__dict__


class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def to_json(self):
        books_json = [book.to_json() for book in self.books]

        return json.dumps(books_json, indent=4)


book_collection = BookCollection()
book_collection.add_book(Book('Abai', 'Mukhtar Auezov', 1942))
book_collection.add_book(Book('Thomas\' Calculus', 'Thomas Jr., George B.', 1951))

books_json = book_collection.to_json()
print(books_json)

