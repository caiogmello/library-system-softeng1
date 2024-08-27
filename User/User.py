from typing import Final

from Book.Book import Book
from Operation.Loan import Loan
from Operation.Reservation import Reservation
from Operation.Devolution import Devolution
from Operation.Exception import OperationException

class User:
    id: str
    name: str
    maxLoanTimeDays: int
    maxOpenLoanOperations: int
    maxReservedBooks: Final[int] = 3
    reservedBooks: int
    loanOperation: Loan
    reserveOperation: Reservation = Reservation()
    devolutionOperation: Devolution = Devolution()
    loanedBooks: list[Book]
    reservedBooks: list[Book]

    def loanBook(self, book: Book) -> None:
        # might raise OperationException
        self.loanOperation.exec(book, self.maxLoanTimeDays)
        self.loanedBooks.append(book)

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
