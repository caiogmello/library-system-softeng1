from abc import ABC, abstractmethod
from Book.Book import Book

class Loan(ABC):

    @abstractmethod
    def exec(self, book:Book, maxLoanTimeDays: int) -> None:
        pass

