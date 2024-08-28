from Operation.Operation import Operation
from Operation.Exception import OperationException
from Book.BookItem import BookItem
from Library.Library import Library
from User.User import User

class Devolution(Operation):
    
    @staticmethod
    def exec(user:User, bookId:int) -> BookItem:
        library = Library.getLibrary()
        book = library.getBookById(bookId)

        if not user.hasLoan(bookId):
            raise OperationException(
                operationType=Devolution,
                user=user,
                bookId=bookId,
                reason="O usuário não possui um empréstimo em aberto do livro",
            )
        
        # TODO: mensagem de sucesso

        return library.devolutionBook(user, bookId)