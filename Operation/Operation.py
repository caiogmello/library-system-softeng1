from abc import ABC, abstractmethod

from Book.Book import Book

class Operation(ABC):
    """
    This operation performs the operation on the item (book) only.
    (updating the book's number of available copies, for example)
    """
    def exec(self, book: Book) -> None:
        """
        Execute operation issued.
        """
        pass