from typing import Final

from Book.BookItem import BookItem
from Operation.Loan import Loan
from Operation.Reservation import Reservation
from Operation.Devolution import Devolution
from Operation.Exception import OperationException
from User.UserState import UserState
from User.UserNotIndebted import UserNotIndebted
from User.UserIndebted import UserIndebted

class User:
    id: str
    name: str
    maxLoanTimeDays: int
    maxOpenLoanOperations: int | None   # None em caso de não haver limite
    maxReservedBooks: Final[int] = 3
    loanOperation: Loan
    reserveOperation: Reservation
    devolutionOperation: Devolution
    loanedBooks: list[BookItem]
    reservedBooks: list[BookItem]
    userState: UserState

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
        self.userState = UserNotIndebted()

    def loanBook(self, book: Book) -> None:
        self.userState.loanBook(self, book)
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

    def makeIndebted(self) -> None:
        self.userState = UserIndebted()

    def makeNotIndebted(self) -> None:
        self.userState = UserNotIndebted()

    def hasReservation(self, bookId: int) -> bool:
        hasReserved = False
        for reservation in self.reservedBooks:
            hasReserved = hasReserved or reservation.getBookId() == bookId
        return hasReserved
    
    def hasLoan(self, bookId: int) -> bool:
        hasLoaned = False
        for loan in self.loanedBooks:
            hasLoaned = hasLoaned or loan.getBookId() == bookId
        return hasLoaned

