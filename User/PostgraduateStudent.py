from User.User import User
from Operation.Loan.PostgraduateLoan import PostgraduateLoan

class PostgraduateStudent(User):
    def __init__(self, id: str, name: str):
        super().__init__(id, name)
        self.maxLoanTimeDays = 5
        self.maxOpenLoanOperations = 4
        self.loanOperation = PostgraduateLoan()
