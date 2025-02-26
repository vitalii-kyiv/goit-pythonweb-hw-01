from abc import ABC, abstractmethod
import logging
from typing import List


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title: str = title
        self.author: str = author
        self.year: str = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class SearchableLibraryInterface(ABC):
    @abstractmethod
    def search_by_author(self, author: str) -> None:
        pass


class BaseLibrary(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logging.info(f"Book '{book.title}' added to the library.")

    def remove_book(self, title: str) -> None:
        initial_count = len(self.books)
        self.books = [book for book in self.books if book.title != title]
        if len(self.books) < initial_count:
            logging.info(f"Book '{title}' removed from the library.")
        else:
            logging.info(f"Book '{title}' not found in the library.")

    def show_books(self) -> None:
        if not self.books:
            logging.info("Library is empty.")
        else:
            logging.info("Library books:")
            for book in self.books:
                logging.info(str(book))


class BookLibrary(BaseLibrary, SearchableLibraryInterface):
    def search_by_author(self, author: str) -> None:
        found_books: List[Book] = [book for book in self.books if book.author == author]

        if found_books:
            logging.info(f"Books by {author}:")
            for book in found_books:
                logging.info(str(book))
        else:
            logging.info(f"No books found by {author}.")


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library: LibraryInterface = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()

    def search_by_author(self) -> None:
        if isinstance(self.library, SearchableLibraryInterface):
            author: str = input("Enter author name to search: ").strip()
            self.library.search_by_author(author)
        else:
            logging.info("This library does not support search by author.")


def main() -> None:
    library: BookLibrary = BookLibrary()
    manager: LibraryManager = LibraryManager(library)

    while True:
        command: str = (
            input("Enter command (add, remove, show, search, exit): ").strip().lower()
        )

        match command:
            case "add":
                title: str = input("Enter book title: ").strip()
                author: str = input("Enter book author: ").strip()
                year: str = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title: str = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "search":
                manager.search_by_author()
            case "exit":
                break
            case _:
                logging.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
