from Operation.Operation import Operation
from Operation.Exception import OperationException
from Book.BookItem import BookItem
from Library.Library import Library
from User.User import User

class Reservation(Operation):
    
    @staticmethod
    def exec(user:User, bookId:int) -> BookItem:
        library = Library.getLibrary()

        if len(user.reservedBooks) >= user.maxReservedBooks:
            raise OperationException(
                operationType=Reservation,
                user=user,
                bookId=bookId,
                reason=f"O usuário já reservou o número máximo de livros ({user.maxReservedBooks})",
            )
        
        # TODO: mensagem de sucesso	
        
        return library.reserveBook(user, bookId)