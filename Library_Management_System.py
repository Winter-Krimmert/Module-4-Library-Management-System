import re
import mysql.connector
from Validation import validate_isbn, validate_library_id, validate_date
from books import Book, FictionBook, NonFictionBook
from users import User
from authors import Author
from genres import Genre

books = []
users = []
authors = []
genres = []

def main_menu():
    while True:
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")
        choice = input("Select an option: ")

        if choice == '1':
            book_operations()
        elif choice == '2':
            user_operations()
        elif choice == '3':
            author_operations()
        elif choice == '4':
            genre_operations()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def book_operations():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            display_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def user_operations():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            view_user_details()
        elif choice == '3':
            display_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def author_operations():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_author()
        elif choice == '2':
            view_author_details()
        elif choice == '3':
            display_authors()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def genre_operations():
    while True:
        print("\nGenre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_genre()
        elif choice == '2':
            view_genre_details()
        elif choice == '3':
            display_genres()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN (e.g., 978-1234567890): ")
    if not validate_isbn(isbn):
        print("Invalid ISBN format. Please try again.")
        return
    publication_date = input("Enter book publication date (YYYY-MM-DD): ")
    if not validate_date(publication_date):
        print("Invalid date format. Please try again.")
        return
    book_type = input("Enter book type (Fiction/Non-Fiction): ")

    try:
        if book_type.lower() == 'fiction':
            book = FictionBook(title, author, isbn, publication_date)
        elif book_type.lower() == 'non-fiction':
            book = NonFictionBook(title, author, isbn, publication_date)
        else:
            print("Invalid book type. Please enter 'Fiction' or 'Non-Fiction'.")
            return


        books.append(book)
        print(f"Book '{title}' added successfully.")
    except Exception as e:
        print(f"An error occurred while adding the book: {e}")

def borrow_book():
    isbn = input("Enter ISBN of the book to borrow: ")
    if not validate_isbn(isbn):
        print("Invalid ISBN format. Please try again.")
        return
    user_id = input("Enter your library ID: ")
    if not validate_library_id(user_id):
        print("Invalid library ID format. Please try again.")
        return

    book = next((b for b in books if b.get_isbn() == isbn), None)
    user = next((u for u in users if u.get_library_id() == user_id), None)

    if book and user:
        try:
            if user.borrow_book(book):
                print(f"Book '{book.get_title()}' borrowed successfully.")
            else:
                print("Book is already borrowed.")
        except Exception as e:
            print(f"An error occurred while borrowing the book: {e}")
    else:
        print("Book or user not found.")

def return_book():
    isbn = input("Enter ISBN of the book to return: ")
    if not validate_isbn(isbn):
        print("Invalid ISBN format. Please try again.")
        return
    user_id = input("Enter your library ID: ")
    if not validate_library_id(user_id):
        print("Invalid library ID format. Please try again.")
        return

    book = next((b for b in books if b.get_isbn() == isbn), None)
    user = next((u for u in users if u.get_library_id() == user_id), None)

    if book and user:
        try:
            if user.return_book(book):
                print(f"Book '{book.get_title()}' returned successfully.")
            else:
                print("Book was not borrowed by you.")
        except Exception as e:
            print(f"An error occurred while returning the book: {e}")
    else:
        print("Book or user not found.")

def search_book():
    isbn = input("Enter ISBN of the book to search: ")
    if not validate_isbn(isbn):
        print("Invalid ISBN format. Please try again.")
        return
    book = next((b for b in books if b.get_isbn() == isbn), None)
    if book:
        print(book)
    else:
        print("Book not found.")

def display_books():
    if books:
        for book in books:
            print(book)
    else:
        print("No books available.")

def add_user():
    name = input("Enter user name: ")
    library_id = input("Enter user library ID (5 digits): ")
    if not validate_library_id(library_id):
        print("Invalid library ID format. Please try again.")
        return
    try:
        user = User(name, library_id)
        users.append(user)
        print(f"User '{name}' added successfully.")
    except Exception as e:
        print(f"An error occurred while adding the user: {e}")

def view_user_details():
    user_id = input("Enter user library ID: ")
    if not validate_library_id(user_id):
        print("Invalid library ID format. Please try again.")
        return
    user = next((u for u in users if u.get_library_id() == user_id), None)
    if user:
        print(user)
    else:
        print("User not found.")

def display_users():
    if users:
        for user in users:
            print(user)
    else:
        print("No users available.")

def add_author():
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    try:
        author = Author(name, biography)
        authors.append(author)
        print(f"Author '{name}' added successfully.")
    except Exception as e:
        print(f"An error occurred while adding the author: {e}")

def view_author_details():
    name = input("Enter author name: ")
    author = next((a for a in authors if a.get_name() == name), None)
    if author:
        print(author)
    else:
        print("Author not found.")

def display_authors():
    if authors:
        for author in authors:
            print(author)
    else:
        print("No authors available.")

def add_genre():
    name = input("Enter genre name: ")
    description = input("Enter genre description: ")
    category = input("Enter genre category: ")
    try:
        genre = Genre(name, description, category)
        genres.append(genre)
        print(f"Genre '{name}' added successfully.")
    except Exception as e:
        print(f"An error occurred while adding the genre: {e}")

def view_genre_details():
    name = input("Enter genre name: ")
    genre = next((g for g in genres if g.get_name() == name), None)
    if genre:
        print(genre)
    else:
        print("Genre not found.")

def display_genres():
    if genres:
        for genre in genres:
            print(genre)
    else:
        print("No genres available.")

if __name__ == "__main__":
    main_menu()
