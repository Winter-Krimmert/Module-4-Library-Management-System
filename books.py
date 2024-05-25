class Book:
    def __init__(self, title, author, isbn, publication_date):
        # marking the attributes as private enforces encapulation. Making the attributes unaccessible from outside the class.
        # this protects the internal state of the object. 
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__publication_date = publication_date
        self.__is_borrowed = False

# no book should default start as checked out. borrow is not a parameter of the book class since we do not need to
# specify the borrow status when a new book is created.



# accessor methods, commonly known as getters, return the value of the private attributes.
# Getters provide a controlled way to access the attributes.
# This preserves the integrity of the data from outside

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
    def get_publication_date(self):
        return self.__publication_date
    
    def is_borrowed(self):
        return self.__is_borrowed
    
    def borrow(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            return True
        return False



# to return object in _str__
    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}, " \
                f"Publication Date: {self.__publication_date}, Borrowed: {'Yes' if self.__is_borrowed else 'No'}"

# Here I am creating a subclass of Book. first I define the subclass, which extends or customizes (i.e. can add additional attributes or initialization steps)
# the subclass from the parent class.
class FictionBook(Book):
    def __init__(self, title, author, isbn, publication_date):
        super().__init__(title, author, isbn, publication_date) 
# now that we are inside an instance of the subclass(we have defined the subclass)
# we must now call the parent class so the subclass can pass to the parent class's constructor

class NonFictionBook(Book):
    def __init__(self, title, author, isbn, publication_date):
        super().__init__(title, author, isbn, publication_date)