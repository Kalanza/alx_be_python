class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def is_checked_out(self):
        return self.is_checked_out
    
    def check_out(self):
        self.is_checked_out = True

    def return_book(self):
        self.is_checked_out = False

class Library:
    def __init__(self):
        self._books = []  # Using private convention with underscore
    
    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                return True
        return False
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                return True
        return False
    
    def list_available_books(self):
        return [book for book in self._books if not book.is_checked_out()]