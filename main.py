import logging
from book import BookManager
from user import UserManager
from check import CheckoutManager
from storage import Storage


def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. List Users")
    print("5. Checkout Book")
    print("6. Checkin Book")
    print("7. Exit")
    choice = input("Enter choice: ")
    return choice


def main():
    storage = Storage("library_data.json")
    book_manager = BookManager(storage)
    user_manager = UserManager(storage)
    checkout_manager = CheckoutManager(book_manager, user_manager, storage)

    while True:
        try:
            choice = main_menu()
            if choice == '1':
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                book_manager.add_book(title, author, isbn)
                print("Book added.")
            elif choice == '2':
                book_manager.list_books()
            elif choice == '3':
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                user_manager.add_user(name, user_id)
                print("User added.")
            elif choice == '4':
                user_manager.list_users()
            elif choice == '5':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkout: ")
                if checkout_manager.checkout_book(user_id, isbn):
                    print("Book checked out.")
                else:
                    print("Failed to checkout book.")
            elif choice == '6':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkin: ")
                if checkout_manager.checkin_book(user_id, isbn):
                    print("Book checked in.")
                else:
                    print("Failed to checkin book.")
            elif choice == '7':
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    main()
