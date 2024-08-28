from Operation.Loan.Loan import Loan
from Library.Library import Library
from Operation.Exception import OperationException

class StudentLoan(Loan):
    def exec(self, user, bookId) -> None:
        # user : User type
        library = Library.getLibrary()

        if len(user.loanedBooks) >= user.maxOpenLoanOperations:
            raise OperationException(
                operationType=StudentLoan,
                user=user,
                bookId=bookId,
                reason=f"O usuário já possui o número máximo de empréstimos abertos ({user.maxOpenLoanOperations})",
            )

        numReservations = len(library.getReservations(bookId))
        numAvailable = len(library.getBookById(bookId).getCopies())

        # i
        if numAvailable == 0:
            raise OperationException(
                operationType=StudentLoan,
                user=user,
                bookId=bookId,
                reason="Não há cópias disponíveis para empréstimo",
            )

        # iii
        if len(user.loanedBooks) >= user.maxOpenLoanOperations:
            raise OperationException(
                operationType=StudentLoan,
                user=user,
                bookId=bookId,
                reason=f"O usuário já possui o número máximo de empréstimos abertos ({user.maxOpenLoanOperations})",
            )

        # iv-v
        if numReservations >= numAvailable and (not user.hasReservation(bookId)):
            raise OperationException(
                operationType=StudentLoan,
                user=user,
                bookId=bookId,
                reason="Não há cópias disponíveis para empréstimo, e não há reserva do usuário",
            )

        if user.hasLoan(bookId):
            raise OperationException(
                operationType=StudentLoan,
                user=user,
                bookId=bookId,
                reason="O usuário já possui um empréstimo do livro",
            )

        library.loanBook(user=user, bookId=bookId, loanTimeDays=user.maxLoanTimeDays)
