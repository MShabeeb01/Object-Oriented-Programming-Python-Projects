import json
import os

# Book class
class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def display_info(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")

    # Convert Book object to dictionary (for JSON)
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "is_borrowed": self.is_borrowed
        }


class Library:
    def __init__(self, filename="library.json"):
        self.books = []
        self.filename = filename
        self.load_books()  # Load saved data if available

    # Save books to JSON
    def save_books(self):
        with open(self.filename, "w") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=4)

    # Load books from JSON
    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.books = [Book(**book) for book in data]

    def add_book(self, title, author):
        # Prevent duplicate entries
        for book in self.books:
            if book.title == title and book.author == author:
                print(f"Book '{title}' by {author} already exists in the library.")
                return
        new_book = Book(title, author)
        self.books.append(new_book)
        self.save_books()
        print(f"Book '{title}' by {author} added to the library.")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\n--- Library Catalog ---")
            for book in self.books:
                book.display_info()

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                self.save_books()
                print(f"Book '{title}' has been borrowed. Enjoy Reading!")
                return
        print(f"Book '{title}' is not available for borrowing.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                self.save_books()
                print(f"Book '{title}' has been returned. Thank you!")
                return
        print(f"Book '{title}' is not in the library or was never borrowed.")


# Main Program
library = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        library.add_book(title, author)
    elif choice == "2":
        library.view_books()
    elif choice == "3":
        title = input("Enter book title to borrow: ").strip()
        library.borrow_book(title)
    elif choice == "4":
        title = input("Enter book title to return: ").strip()
        library.return_book(title)
    elif choice == "5":
        print("Exiting the library management system. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-5).")



# ---------------- File Handling in Python(JSON)----------------

# 1. open(file, mode)
#    - Opens a file and returns a file object.
#    - file  → name of the file (example: "library.json")
#    - mode  → how you want to use the file:
#        "r" → read mode (default). Error if file doesn’t exist.
#        "w" → write mode. Creates a new file or overwrites existing.
#        "a" → append mode. Adds new data to the end of file.
#        "x" → exclusive creation. Error if file already exists.
#        "rb"/"wb" → read/write in binary mode.

# 2. with open(filename, mode) as f:
#    - 'with' is a context manager → automatically closes the file.
#    - 'f' is the file object (a handle you use to read/write).

# Example:
# with open("library.json", "w") as f:
#     f.write("Hello Library")
#
# Explanation of example:
# - "library.json" is opened in write mode ("w").
# - f is the file object used to interact with the file.
# - f.write("Hello Library") writes text into the file.
# - After the block ends, Python automatically closes the file.

# 3. In JSON usage:
# with open("library.json", "w") as f:
#     json.dump(data, f, indent=4)   # Save Python data into file in JSON format
#
# with open("library.json", "r") as f:
#     data = json.load(f)            # Load JSON data back into Python objects
