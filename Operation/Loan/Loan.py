from Loan.LoanType import LoanType

class Loan:
    def __init__(self, loan_type: LoanType) -> None:
        self._loan_type: LoanType = loan_type

