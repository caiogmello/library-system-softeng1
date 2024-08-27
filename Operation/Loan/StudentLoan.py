from Operation.Loan.Loan import Loan
from Book.Book import Book

class StudentLoan(Loan):
    def exec(self, book:Book) -> None:
        return super().exec(book)