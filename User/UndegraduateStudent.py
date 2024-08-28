from User.User import User
from Operation.Loan.StudentLoan import StudentLoan
from Operation.Reservation import Reservation
from Operation.Devolution import Devolution

class UndegraduateStudent(User):
    def __init__(self, id: str, name: str):
        super().__init__(id, name)
        self.maxLoanTimeDays = 3
        self.maxOpenLoanOperations = 3
        self.loanOperation = StudentLoan()

    def loanBook(self, bookId: int) -> None:
        bookcopy = self.userState.loanBook(self, bookId)
        self.loanedBooks.append(bookcopy)
        if bookcopy in self.reservedBooks:
            self.reservedBooks.remove(bookcopy)

    def reserveBook(self, bookId: int) -> None:
        bookCopy = Reservation().exec(self, bookId)
        self.reservedBooks.append(self, bookCopy)
    
    def returnBook(self, bookId: int) -> None:
        bookCopy = Devolution().exec(self, bookId)
        self.loanedBooks.remove(bookCopy)