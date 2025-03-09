from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, book_id):
        self.__title = title
        self.__author = author
        self.__book_id = book_id
        self.__is_borrowed = False

    def borrow(self):
        self.__is_borrowed = True
        return f"{self.__title} has been borrowed."

    def return_book(self):
        self.__is_borrowed = False
        return f"{self.__title} has been returned."

    @abstractmethod
    def display_info(self):
        pass

    def get_title(self):
        return self.__title

class HardBook(Book):
    def __init__(self, title, author, book_id, pages):
        super().__init__(title, author, book_id)
        self.pages = pages

    def display_info(self):
        return f"{self.get_title()} has {self.pages} pages."


class SoftBook(Book):
    def __init__(self, title, author, book_id, file_size):
        super().__init__(title, author, book_id)
        self.file_size = file_size

    def display_info(self):
        return f"{self.get_title()} has a size of {self.file_size}MB."

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        book.borrow()
        return f"{self.name} borrowed {book.get_title()}"

    def return_book(self, book):
        self.borrowed_books.remove(book)
        book.return_book()
        return f"{self.name} returned {book.get_title()}"

class Librarian(User):
    def add_book(self, book_list, book):
        book_list.append(book)
        return  f"Librarian {self.name} added '{book.get_title()}' to the library."


def main():
    book1 = HardBook("Rich Dad Poor Dad", "Robert T. Kiyosaki", 1, 100)
    book2 = SoftBook("Think And Grow Rich", "Napoleon Hill", 2, 2)

    member = User("Uzair")
    librarian = Librarian("Mr.Hassan")

    library_books = []

    print(librarian.add_book(library_books, book1))
    print(librarian.add_book(library_books, book2))

    print(book1.display_info())
    print(book2.display_info())

    print(member.borrow_book(book1))
    print(member.borrow_book(book2))

    print(member.return_book(book2))
    print(member.return_book(book1))

if __name__ == "__main__":
    main()