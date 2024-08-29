from Operation.Operation import Operation
from Book.BookItem import BookItem
import Library.Library as lib

class CancelReservationIfExists(Operation):
    @staticmethod
    def exec(user, bookId: int) -> BookItem | None:
        library = lib.Library.getLibrary()

        if user.hasReservation(bookId):
            return library.unreserveBook(user, bookId)
