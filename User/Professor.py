from User.User import User
from Book.Book import Book
from Observer.Observer import Observer
from Operation.Loan.ProfessorLoan import ProfessorLoan
from Operation.Exception import OperationException
from Operation.Reservation import Reservation
from Operation.Devolution import Devolution

class Professor(User, Observer):
    _dupReservationNotificationCnt: int

    def __init__(self, id: str, name: str):
        super().__init__(id, name)
        self.maxLoanTimeDays = 7
        self.maxOpenLoanOperations = None
        self.loanOperation = ProfessorLoan()
        self._dupReservationNotificationCnt = 0

    def loanBook(self, bookId: int) -> None:
        bookCopy = self.userState.loanBook(self, bookId)
        self.loanedBooks.append(bookCopy)
        if bookCopy in self.reservedBooks:
            self.reservedBooks.remove(bookCopy)

    def reserveBook(self, bookId: int) -> None:
        bookCopy = Reservation().exec(self, bookId)
        self.reservedBooks.append(self, bookCopy)
    
    def returnBook(self, bookId: int) -> None:
        bookCopy = Devolution().exec(self, bookId)
        self.loanedBooks.remove(bookCopy)

    def update(self, observedBook: Book):
        self._dupReservationNotificationCnt += 1

    def getNotificationCount(self) -> int:
        return self._dupReservationNotificationCnt
    