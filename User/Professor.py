from User.User import User
from Book.Book import Book
from Observer.Observer import Observer
from Operation.Loan.ProfessorLoan import ProfessorLoan

class Professor(User, Observer):
    dupReservationNotificationCnt: int

    def __init__(self, id: str, name: str):
        super().__init__(id, name)
        self.maxLoanTimeDays = 7
        self.maxOpenLoanOperations = None
        self.loanOperation = ProfessorLoan()
        self.dupReservationNotificationCnt = 0

    def update(self, observedBook: Book):
        self.dupReservationNotificationCnt += 1
