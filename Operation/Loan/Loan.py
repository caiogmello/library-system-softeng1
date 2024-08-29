from abc import ABC, abstractmethod
from Operation.Operation import Operation

from Book.BookItem import BookItem

class Loan(Operation, ABC):
    @abstractmethod
    def exec(self, user: "User", bookId: int) -> BookItem:
        """
        Try to loan a book from the library.
        Print error message in case of failure.
        """
        pass

