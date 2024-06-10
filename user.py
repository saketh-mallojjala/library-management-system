import logging


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f"Name: {self.name}, User ID: {self.user_id}"


class UserManager:
    def __init__(self, storage):
        self.storage = storage
        self.users = self.storage.load_users()

    def add_user(self, name, user_id):
        if self.find_user(user_id):
            raise ValueError("A user with this ID already exists.")
        user = User(name, user_id)
        self.users.append(user)
        self.storage.save_users(self.users)
        logging.info(f"Added user: {user}")

    def list_users(self):
        for user in self.users:
            print(user)

    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def update_user(self, user_id, name=None):
        user = self.find_user(user_id)
        if user:
            if name:
                user.name = name
            self.storage.save_users(self.users)
            logging.info(f"Updated user: {user}")
            return True
        return False

    def delete_user(self, user_id):
        user = self.find_user(user_id)
        if user:
            self.users.remove(user)
            self.storage.save_users(self.users)
            logging.info(f"Deleted user: {user}")
            return True
        return False
