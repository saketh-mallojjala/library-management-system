# Library Management System

This project implements a simple Library Management System in Python. The system allows users to manage books, users, and book checkouts through a command-line interface (CLI). It provides functionalities such as adding, updating, deleting, listing, checking out, and checking in books, as well as adding and listing users.

## Features

- **Manage Books**: Add, update, delete, list, and search books by various attributes like title, author, or ISBN.
- **Manage Users**: Add, update, delete, list, and search users by attributes like name or user ID.
- **Checkout and Check-in Books**: Allow users to check out and check in books, tracking book availability.
- **Simple Logging**: Log operations performed on books and users.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/library-management-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd library-management-system
    ```



## Usage

1. Run the `main.py` script:

    ```bash
    python main.py
    ```

2. Follow the on-screen prompts to perform various operations such as adding books, adding users, checking out books, and checking in books.

## File Structure

- **main.py**: Main entry point for the application, handles user interactions.
- **book.py**: Contains classes and methods for managing books.
- **user.py**: Contains classes and methods for managing users.
- **check.py**: Implements the checkout and check-in functionality.
- **storage.py**: Handles file-based storage for storing data.
- **models.py**: Defines data models for books, users, and checkouts.
- **library_data.json**: JSON file for storing data persistently.

## Documentation

- **main.py**: Contains the main entry point for the application. It displays a menu and handles user inputs to perform various operations.
- **book.py**: Defines the `Book` class and `BookManager` class for managing books. It provides methods for adding, updating, deleting, listing, and searching books.
- **user.py**: Defines the `User` class and `UserManager` class for managing users. It provides methods for adding, updating, deleting, listing, and searching users.
- **check.py**: Defines the `CheckoutManager` class for managing book checkouts. It provides methods for checking out and checking in books, tracking book availability, and user validation.
- **storage.py**: Defines the `Storage` class for file-based storage. It provides methods for loading and saving data to a JSON file.
- **models.py**: Contains data models for books, users, and checkouts. It defines classes for `Book`, `User`, and `Checkout`.
  
