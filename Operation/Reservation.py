from Operation.Operation import Operation
from Operation.Exception import OperationException
from Book.BookItem import BookItem
import Library.Library as lib

class Reservation(Operation):
    
    @staticmethod
    def exec(user, bookId:int) -> BookItem:
        library = lib.Library.getLibrary()

        if len(user.reservedBooks) >= user.maxReservedBooks:
            raise OperationException(
                operationType=Reservation,
                user=user,
                bookId=bookId,
                reason=f"O usuário já reservou o número máximo de livros ({user.maxReservedBooks})",
            )
                
        return library.reserveBook(user, bookId)