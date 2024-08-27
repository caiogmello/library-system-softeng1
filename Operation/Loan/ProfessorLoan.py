from Operation.Loan.Loan import Loan
from Library.Library import Library
from Book.Book import Book

class ProfessorLoan(Loan):
    def exec(self, book: Book) -> None:            
        return super().exec(book, 7)