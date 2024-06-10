import logging


class CheckoutManager:
    def __init__(self, book_manager, user_manager, storage):
        self.book_manager = book_manager
        self.user_manager = user_manager
        self.storage = storage
        self.checkouts = self.storage.load_checkouts()

    def checkout_book(self, user_id, isbn):
        user = self.user_manager.find_user(user_id)
        if not user:
            raise ValueError("User not found.")

        book = self.book_manager.find_book(isbn)
        if not book:
            raise ValueError("Book not found.")

        if not book.available:
            raise ValueError("Book is not available for checkout.")

        book.available = False
        self.checkouts.append({"user_id": user_id, "isbn": isbn})
        self.storage.save_checkouts(self.checkouts)
        self.book_manager.storage.save_books(self.book_manager.books)
        logging.info(f"Checked out book: {isbn} to user: {user_id}")
        return True

    def checkin_book(self, user_id, isbn):
        user = self.user_manager.find_user(user_id)
        if not user:
            raise ValueError("User not found.")

        book = self.book_manager.find_book(isbn)
        if not book:
            raise ValueError("Book not found.")

        checkout_exists = False
        for checkout in self.checkouts:
            if checkout["user_id"] == user_id and checkout["isbn"] == isbn:
                checkout_exists = True
                break

        if not checkout_exists:
            raise ValueError("This book is not checked out by the user.")

        book.available = True
        self.checkouts = [checkout for checkout in self.checkouts if
                          not (checkout["user_id"] == user_id and checkout["isbn"] == isbn)]
        self.storage.save_checkouts(self.checkouts)
        self.book_manager.storage.save_books(self.book_manager.books)
        logging.info(f"Checked in book: {isbn} from user: {user_id}")
        return True
