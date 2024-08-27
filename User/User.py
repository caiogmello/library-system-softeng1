from typing import Final

from abc import ABC, abstractmethod

from Book.Book import Book
from Operation.Loan.Loan import Loan
from Operation.Reservation import Reservation
from Operation.Devolution import Devolution
from Operation.Exception import OperationException

class User(ABC):
    id: str
    name: str
    maxLoanTimeDays: int
    maxOpenLoanOperations: int | None   # None em caso de não haver limite
    maxReservedBooks: Final[int] = 3
    loanOperation: Loan
    reserveOperation: Reservation
    devolutionOperation: Devolution
    loanedBooks: list[Book]
    reservedBooks: list[Book]

    def __init__(
        self,
        id: str,
        name: str
    ):
        self.id = id
        self.name = name
        self.reserveOperation = Reservation()
        self.devolutionOperation = Devolution()
        self.loanedBooks = []
        self.reservedBooks = []

    @abstractmethod
    def loanBook(self, book: Book) -> None:
       pass

    @abstractmethod
    def reserveBook(self, book: Book) -> None:
        pass
    
    @abstractmethod
    def returnBook(self, book: Book) -> None:
        pass
