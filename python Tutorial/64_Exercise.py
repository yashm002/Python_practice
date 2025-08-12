class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def showInfo(self):
        print(f"The library has {self.no_of_books} books. The names are:")
        for book in self.books:
            print(book)

lb = Library()
lb.addBook("Harry Potter")
lb.addBook("Deep Work")
lb.showInfo()
