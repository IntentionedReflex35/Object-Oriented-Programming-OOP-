# Building a library management system with OOP

from abc import ABC, abstractmethod


class Books:
    def __init__(self, title, author, isbn, is_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__is_available = bool(is_available)

    # Getter method, a clean to get or read encapsulated attributes
    def is_book_available(self):
        return self.__is_available

    # Here, one wants to borrow a book. A book can be borrowed only if it is available.
    # self.__is_available will be set as false to make it unavailable at all times.
    def borrow_book(self):
        if self.__is_available:
            self.__is_available = False
            print(f"The book, {self.title} by {self.author} has been borrowed.")
        else:
            print(f"{self.title} is not available.")

    # One wants to return a book. A book can be returned regardless if it's available or not.
    def return_book(self):
        self.__is_available = True
        print(f"The book, {self.title} by {self.author} with ISBN, {self.isbn} has been returned.")


class Members(ABC):
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    @abstractmethod
    def borrow(self, book):       # Books borrowed will be added to the list
        self.borrowed_books.append(book)

    def return_(self, book):       # Books returned will be removed from the list
        self.borrowed_books.remove(book)
        print(f"This book {book} has been returned.")

    @abstractmethod
    def get_member_info(self):
        pass


class RegularMember(Members):
    def borrow(self, book):  # Can only borrow a maximum of 3 books
        max_books = 3
        if len(self.borrowed_books) >= max_books:      # Add condition to check for breach
            print(f"Maximum number of books({max_books}) reached.")
            return
        super().borrow(book)                           # Add book to the list
        print(f"{book} borrowed successfully!")

    def get_member_info(self):
        print(f"Name: {self.name}\n"
              f"Member ID: {self.member_id}\n"
              f"Status: Regular Member\n"
              f"Books Borrowed: "
              f"{len(self.borrowed_books)}/{3}")


class PremiumMember(Members):
    def borrow(self, book):    # Can only borrow a maximum of ten books
        max_books = 10
        if len(self.borrowed_books) >= max_books:
            print(f"Maximum number of books({max_books}) reached.")
            return
        super().borrow(book)
        print(f"{book} borrowed successfully!")

    def get_member_info(self):
        print(f"Name: {self.name}\n"
              f"Member ID: {self.member_id}\n"
              f"Status: Premium Member\n"
              f"Books Borrowed: "
              f"{len(self.borrowed_books)}/{10}")


class Library:
    def __init__(self):
        self.book_list = []
        self.member_list = []

    def add_book(self, book):
        self.book_list.append(book)
        print(f"This book {book} has been added to the shelf.")

    def register_members(self, member):
        self.member_list.append(member)
        print(f"Welcome, {member}, to the Library.")

    def available_books(self):
        available = [book.title for book in self.book_list if book.is_book_available()]
        if available:
            print("Available books:", available)
        else:
            print("No books available right now.")


# Create Book objects
book1 = Books("Legend Of The Seeker", "Terry Goodkind", "LB001", True)
book2 = Books("Marvel", "Stan Lee", "MV002", True)
book3 = Books("America", "Jon Meachem", "AM003", True)
book4 = Books("Daredevil", "Stan Lee", "MV003", True)
book5 = Books("Hulk", "Stan Lee", "MV004", True)
book6 = Books("Captain America", "Stan Lee", "MV005", True)
book7 = Books("Iron Man", "Stan Lee", "MV006", True)
book8 = Books("Black Panther", "Stan Lee", "MV007", True)

# Create one Library
library = Library()

# Create member objects
member1 = RegularMember("Ivan", "st.235")
member2 = PremiumMember("Jayden", "st.356")

# Register members
library.register_members(member1)
print()
library.register_members(member2)
print("===============================================================================================================")
# Add books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)
library.add_book(book7)
library.add_book(book8)
library.add_book(book6)
print("===============================================================================================================")
# Member borrows through the library
book1.borrow_book()    # Verifying if available or not
member1.borrow(book1.title)
member1.borrow(book2.title)
member1.borrow(book3.title)
member1.borrow(book4.title)
print()
member2.borrow(book5.title)
member2.borrow(book1.title)
print("===============================================================================================================")
# Member Information
member1.get_member_info()
print()
member2.get_member_info()
print("===============================================================================================================")
# Check available books
library.available_books()
