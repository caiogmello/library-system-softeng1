from Operation.Loan.LoanType import LoanType

class Loan:
    def __init__(self, loanType: LoanType) -> None:
        self._loanType: LoanType = loanType

