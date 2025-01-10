#Here’s a mini-project idea based on the concept of logging, exception handling, and file management. This exercise will help students apply the concepts in a practical scenario while reinforcing their understanding.

Mini-Project: Library Management System Log Tracker
Problem Statement
Create a program that simulates a library management system where users can:

Borrow books.
Return books.
Check available books.
The program should:

Log all user actions (borrow, return, invalid inputs, etc.) and any exceptions into a log file.
At the end of the program, the log file should be cleared and reset for the next session.

TIPS:-
Setup:

Create a list of books available in the library (e.g., ["Harry Potter", "1984", "To Kill a Mockingbird"]).
Use a dictionary to keep track of which books are borrowed (e.g., {"Harry Potter": False, "1984": True}).
Menu:

Present the user with a menu:
View available books
Borrow a book
Return a book
Exit
Requirements for Each Action:

View Books:
Display all books and their availability.
Borrow a Book:
Check if the book is available. If yes, allow the user to borrow and log the action. If not, log an error.
Return a Book:
Check if the book is borrowed. If yes, mark it as returned and log the action. If not, log an error.
Exit:
Before exiting, clear the log file.
Error Handling:

Handle invalid inputs, such as selecting a book that doesn't exist or entering invalid menu options, and log these errors.
Logging Format:

Use the following format for logs:
ruby
Copy code
%(asctime)s - %(levelname)s - %(message)s
File Management:

Ensure the log file is cleared at the end of the program

books dictionary ->
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
