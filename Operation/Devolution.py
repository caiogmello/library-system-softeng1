from Operation.Operation import Operation
from Operation.Exception import OperationException
from Book.BookItem import BookItem
import Library.Library as lib

class Devolution(Operation):
    
    @staticmethod
    def exec(user: "User", bookId:int) -> BookItem:
        library = lib.Library.getLibrary()
        book = library.getBookById(bookId)

        if not user.hasLoan(bookId):
            raise OperationException(
                operationType=Devolution,
                user=user,
                bookId=bookId,
                reason="O usuário não possui um empréstimo em aberto do livro",
            )
        
        return library.returnBook(user, bookId)