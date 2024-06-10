import logging


class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {'Yes' if self.available else 'No'}"


class BookManager:
    def __init__(self, storage):
        self.storage = storage
        self.books = self.storage.load_books()

    def add_book(self, title, author, isbn):
        if self.find_book(isbn):
            raise ValueError("A book with this ISBN already exists.")
        book = Book(title, author, isbn)
        self.books.append(book)
        self.storage.save_books(self.books)
        logging.info(f"Added book: {book}")

    def list_books(self):
        for book in self.books:
            print(book)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def update_book(self, isbn, title=None, author=None):
        book = self.find_book(isbn)
        if book:
            if title:
                book.title = title
            if author:
                book.author = author
            self.storage.save_books(self.books)
            logging.info(f"Updated book: {book}")
            return True
        return False

    def delete_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            self.books.remove(book)
            self.storage.save_books(self.books)
            logging.info(f"Deleted book: {book}")
            return True
        return False
