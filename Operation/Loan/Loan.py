from abc import ABC, abstractmethod
from Book.Book import Book
from Library.Library import Library

class Loan(ABC):

    @abstractmethod
    def exec(self, book:Book, maxLoanTimeDays: int, library: Library) -> None:
        pass

