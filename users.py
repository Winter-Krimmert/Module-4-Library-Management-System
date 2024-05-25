class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []
# not including self.__borrowed books as a parameter conforms to good oop design. Ensures the attribute is always initialized to an empty list,
# reprenting a new user without borrowed books.
# encapsulating the attribute prevents outside code from manipulating it and setting it to an arbitrary state. 
# this gives us the ability to control how the attribute is modified (via borrowed_book and return_book methods).

# accessor methods, commonly known as getters, return the value of the private attributes.
# Getters provide a controlled way to access the attributes.
# This preserves the integrity of the data from outside.
    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id

    def borrow_book(self, book):
        if book.borrow():
            self.__borrowed_books.append(book.get_title())
            return True
        return False

    def return_book(self, book):
        if book.return_book():
            self.__borrowed_books.remove(book.get_title())
            return True
        return False

    def get_borrowed_books(self):
        return self.__borrowed_books
    
# For user convenience. For clear summary of the user details. For debugging.
    def __str__(self):
        return f"Name: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {self.__borrowed_books}"
