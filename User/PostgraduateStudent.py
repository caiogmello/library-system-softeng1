from User.User import User
from Book.Book import Book
from Operation.Loan.StudentLoan import StudentLoan
from Operation.Exception import OperationException


class PostgraduateStudent(User):
    def __init__(self, id: str, name: str):
        super().__init__(id, name)
        self.maxLoanTimeDays = 5
        self.maxOpenLoanOperations = 4
        self.loanOperation = StudentLoan()

    def loanBook(self, book: Book) -> None:
        # might raise OperationException
        if (self.maxOpenLoanOperations is not None) and (len(self.loanedBooks) >= self.maxOpenLoanOperations):
            raise OperationException(
                self.loanOperation,
                self,
                book,
                f"O usuário já possui o número máximo de empréstimos abertos ({self.maxOpenLoanOperations})",
            )
        self.loanOperation.exec(book, self.maxLoanTimeDays)
        self.loanedBooks.append(book)
        if book in self.reservedBooks:
            self.reservedBooks.remove(book)


    def reserveBook(self, book: Book) -> None:
        # might raise OperationException
        if len(self.reservedBooks) >= self.maxReservedBooks:
            raise OperationException(
                self.reserveOperation,
                self,
                book,
                f"O usuário já reservou o número máximo de livros ({self.maxReservedBooks})",
            )
        self.reservedBooks.append(book)
        

    def returnBook(self, book: Book) -> None:
        # might raise OperationException
        if book not in self.loanedBooks:
            raise OperationException(
                self.devolutionOperation,
                self,
                book,
                "O livro não foi emprestado para o usuário",
            )
        self.devolutionOperation.exec(book)
        self.loanedBooks.remove(book)