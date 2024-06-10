import json
import logging
from book import Book
from user import User


class Storage:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {"books": [], "users": [], "checkouts": []}

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def load_books(self):
        return [Book(**book_data) for book_data in self.data["books"]]

    def save_books(self, books):
        self.data["books"] = [book.__dict__ for book in books]
        self.save_data()

    def load_users(self):
        return [User(**user_data) for user_data in self.data["users"]]

    def save_users(self, users):
        self.data["users"] = [user.__dict__ for user in users]
        self.save_data()

    def load_checkouts(self):
        return self.data.get("checkouts", [])

    # def save_checkouts(self, checkouts):
    #     self.data["checkouts"] = checkouts
    #     self.save_data()

    def save_checkouts(self, checkouts):
        self.data["checkouts"] = checkouts
        self.save_data()
