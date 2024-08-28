from typing import Final

from Book.BookItem import BookItem
from Operation.Loan import Loan
from Operation.Reservation import Reservation
from Operation.Devolution import Devolution
from User.State.UserState import UserState
from User.State.UserNotIndebted import UserNotIndebted
from User.State.UserIndebted import UserIndebted

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
        self.loanedBooks = []
        self.reservedBooks = []
        self.userState = UserNotIndebted()

    def loanBook(self, bookId: int) -> None:
        bookCopy = self.userState.loanBook(self, bookId)
        self.loanedBooks.append(bookCopy)
        if bookCopy in self.reservedBooks:
            self.reservedBooks.remove(bookCopy)

    def reserveBook(self, bookId: int) -> None:
        bookCopy = Reservation().exec(self, bookId)
        self.reservedBooks.append(bookCopy)
    
    def returnBook(self, bookId: int) -> None:
        bookCopy = Devolution().exec(self, bookId)
        self.removeLoan(bookId)

    def makeIndebted(self) -> None:
        self.userState = UserIndebted()

    def makeNotIndebted(self) -> None:
        self.userState = UserNotIndebted()

    def removeLoan(self, bookId: int) -> None:
        for book in self.loanedBooks:
            if book.getBookId() == bookId:
                self.loanedBooks.remove(book)
                break

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
