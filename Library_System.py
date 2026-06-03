# Building a library management system with OOP

from abc import ABC, abstractmethod


class Books:
    def __init__(self, title, author, isbn, is_available):
        self.title = title.capitalize()
        self.author = author.capitalize()
        self.isbn = isbn
        self.__is_available = bool(is_available)

    # Here, one wants to borrow a book. A book can be borrowed only if it is available.
    def borrow_book(self):
        if self.__is_available:
            print(f"The book, {self.title} by {self.author} has been borrowed.")
        else:
            print(f"Book not available.")

    # One wants to return a book. A book can be returned regardless if it's available or not.
    def return_book(self):
        print(f"The book, {self.title} by {self.author} with ISBN, {self.isbn} is returned.")


class Members(ABC):
    def __init__(self, name, member_id):
        self.name = name.capitalize()
        self.member_id = member_id
        self.borrowed_books = []

    @abstractmethod
    def borrow(self, book):       # Books borrowed will be added to the list
        self.borrowed_books.append(book)

    @abstractmethod
    def return_(self, book):       # Books returned will be removed from the list
        self.borrowed_books.remove(book)
        print(f"This book {book} has been returned.")

    @abstractmethod
    def get_member_info(self):
        number_of_books = len(self.borrowed_books)
        member_status = ['Regular', 'Premium']
        return number_of_books, member_status


class RegularMember(Members):
    def borrow(self, book):  # Can only borrow a maximum of 3 books
        max_books = 3
        super().borrow(book)
        if len(self.borrowed_books) > max_books:
            print(f"Maximum number of books({max_books}) reached. Upgrade to premium to borrow more.")
            print(self.borrowed_books[:-1])
        assert len(self.borrowed_books) <= max_books, f"Books borrowed should at most be {max_books}"

    def return_(self, book):
        super().return_(book)

    def get_member_info(self):
        print(f"Name: {self.name}\nMember_id: {self.member_id}\nNumber of borrowed books: "
              f"{super().get_member_info()[0]}\n"
              f"Member Status: {super().get_member_info()[1][0]}")


class PremiumMember(Members):
    def borrow(self, book):    # Can only borrow a maximum of ten books
        max_books = 10
        super().borrow(book)
        if len(self.borrowed_books) > max_books:
            print(f"Maximum number of books({max_books}) reached. Upgrade to premium to borrow more.")
            print(self.borrowed_books[:-1])
        assert len(self.borrowed_books) <= max_books, f"Books borrowed should at most be {max_books}"

    def return_(self, book):
        pass

    def get_member_info(self):
        print(f"Name: {self.name}\nMember_id: {self.member_id}\nNumber of borrowed books: "
              f"{super().get_member_info()[0]}\n"
              f"Member Status: {super().get_member_info()[1][1]}")


class Library:
    pass


book0 = Books('garde', "john favour", "st235", True)
book0.borrow_book()

member1 = RegularMember("Ivan", "st.235")
member1.borrow("Legend Of The Seeker")
member1.borrow("Marvel")
member1.borrow("America")
member1.return_("Legend Of The Seeker")
# member1.borrow("War")
member1.get_member_info()
print('=====================================================')
member2 = PremiumMember("Arthur", "st.236")
member2.borrow("little")
member2.borrow('sun')
member2.borrow('hey there')
member2.get_member_info()
