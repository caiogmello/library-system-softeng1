from User.User import User
from Operation.Loan.StudentLoan import StudentLoan
from Operation.Reservation import Reservation
from Operation.Devolution import Devolution


class PostgraduateStudent(User):
    def __init__(self, id: str, name: str):
        super().__init__(id, name)
        self.maxLoanTimeDays = 5
        self.maxOpenLoanOperations = 4
        self.loanOperation = StudentLoan()

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
