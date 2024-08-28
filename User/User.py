from typing import Final

from Book.BookItem import BookItem
from Operation.Loan import Loan
from Operation.Reservation import Reservation
from Operation.Devolution import Devolution
from User.UserState import UserState
from User.UserNotIndebted import UserNotIndebted
from User.UserIndebted import UserIndebted

class User:
    id: str
    name: str
    maxLoanTimeDays: int
    maxOpenLoanOperations: Final[int | None]   # None em caso de não haver limite
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

    def loanBook(self, bookId: int) -> None:
        bookcopy = self.userState.loanBook(self, bookId)
        self.loanedBooks.append(bookcopy)
        if bookcopy in self.reservedBooks:
            self.reservedBooks.remove(bookcopy)

    def reserveBook(self, bookId: int) -> None:
        # might raise OperationException
        # TODO reservation operation
        self.reservedBooks.append(self, bookId)
    
    def returnBook(self, bookId: int) -> None:
        # might raise OperationException
        # TODO devolution operation
        bookcopy = self.devolutionOperation.exec(self, bookId)
        self.loanedBooks.remove(bookcopy)

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
