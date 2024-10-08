from User.User import User
from Operation.Loan.StudentLoan import StudentLoan

class UndegraduateStudent(User):
    def __init__(self, id: str, name: str):
        super().__init__(id, name)
        self.maxLoanTimeDays = 3
        self.maxOpenLoanOperations = 3
        self.loanOperation = StudentLoan()
