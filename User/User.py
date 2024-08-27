from typing import Final

from Book.Book import Book
from Operation.Loan.Loan import Loan
from Operation.Reservation import Reservation
from Operation.Devolution import Devolution
from Operation.Exception import OperationException

class User:
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

    def loanBook(self, book: Book) -> None:
        # might raise OperationException
        if (self.maxOpenLoanOperations is not None) and (len(self.loanedBooks) >= self.maxOpenLoanOperations):
            raise OperationException(
                self.loanOperation,
                self,
                book,
                f"O usuário já possui o número máximo de empréstimos abertos ({self.maxOpenLoanOperations})",
            )
        self.loanOperation.exec(book, self.maxLoanTimeDays)
        self.loanedBooks.append(book)
        if book in self.reservedBooks:
            self.reservedBooks.remove(book)

    def reserveBook(self, book: Book) -> None:
        # might raise OperationException
        if len(self.reservedBooks) >= self.maxReservedBooks:
            raise OperationException(
                self.reserveOperation,
                self,
                book,
                f"O usuário já reservou o número máximo de livros ({self.maxReservedBooks})",
            )
        self.reservedBooks.append(book)
    
    def returnBook(self, book: Book) -> None:
        # might raise OperationException
        if book not in self.loanedBooks:
            raise OperationException(
                self.devolutionOperation,
                self,
                book,
                "O livro não foi emprestado para o usuário",
            )
        self.devolutionOperation.exec(book)
        self.loanedBooks.remove(book)
