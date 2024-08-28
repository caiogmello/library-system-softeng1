from Operation.Loan.Loan import Loan
from Library.Library import Library
from Operation.Exception import OperationException

class ProfessorLoan(Loan):
    def exec(self, user, bookId) -> None:
        library = Library.getLibrary()
        numAvailable = len(library.getBookById(bookId).getCopies())

        # i
        if numAvailable == 0:
            raise OperationException(
                operationType=ProfessorLoan,
                user=user,
                bookId=bookId,
                reason="Não há cópias disponíveis para empréstimo",
            )
        
        library.loanBook(user=user, bookId=bookId, loanTimeDays=user.maxLoanTimeDays)
