import time
from logging import *

def clearLogFiles():
    with open(r"C:\Users\pratiksha\OneDrive\Desktop\pythonprogramming\logfile.txt", 'w') as f:
        f.truncate(0)  
    print("Log file is cleared")

def configLogs():
    with open(r"C:\Users\pratiksha\OneDrive\Desktop\pythonprogramming\logfile.txt", 'a+') as f:
        pass
    basicConfig(
        filename=r"C:\Users\pratiksha\OneDrive\Desktop\pythonprogramming\logfile.txt",
        level=INFO,
        format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
    )

books = {
    "Harry Potter": {
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "year": 1997,
        "borrowed": False
    },
    "1984": {
        "author": "George Orwell",
        "genre": "Dystopian",
        "year": 1949,
        "borrowed": False
    },
    "To Kill a Mockingbird": {
        "author": "Harper Lee",
        "genre": "Fiction",
        "year": 1960,
        "borrowed": False
    }
}


def view_books():
    print("\nAvailable Books:")
    for book, details in books.items():
        status = "Available" if not details["borrowed"] else "Borrowed"
        print(f"{book} - {status}")
    info("User viewed books list.")


def borrow_book():
    try:
        book_name = input("\nEnter the name of the book to borrow: ").strip()
        if book_name in books:
            if not books[book_name]["borrowed"]:
                books[book_name]["borrowed"] = True
                print(f"You have borrowed '{book_name}'.")
                info(f"'{book_name}' borrowed successfully.")
            else:
                print(f"'{book_name}' is already borrowed.")
                error(f"Attempt to borrow '{book_name}' failed. Already borrowed.")
        else:
            raise KeyError(f"'{book_name}' is not available in the library.")
    except KeyError as e:
        print(e)
        error(e, exc_info=True)

def return_book():
    try:
        book_name = input("\nEnter the name of the book to return: ").strip()
        if book_name in books:
            if books[book_name]["borrowed"]:
                books[book_name]["borrowed"] = False
                print(f"You have returned '{book_name}'.")
                info(f"'{book_name}' returned successfully.")
            else:
                raise ValueError(f"'{book_name}' was not borrowed.")
        else:
            raise KeyError(f"'{book_name}' is not available in the library.")
    except (KeyError, ValueError) as e:
        print(e)
        error(e, exc_info=True)


def main():
    while True:
        print("\nLibrary Management System")
        print("1. View Available Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: ").strip())
            if choice == 1:
                view_books()
            elif choice == 2:
                borrow_book()
            elif choice == 3:
                return_book()
            elif choice == 4:
                clearLogFiles()
                break
            else:
                raise ValueError("Invalid choice. Please choose between 1 and 4.")
        except ValueError as v:
            print(v)
            error(v, exc_info=True)
        except Exception as e:
            print("An unexpected error occurred.")
            error(e, exc_info=True)

if __name__ == "__main__":
    clearLogFiles()
    configLogs()
    main()
