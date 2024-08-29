from Book.BookItem import BookItem
from User.User import User
from datetime import date
import Library.Library as lib


class ReservationItem:
    _user: User
    _reservedItem: BookItem
    _reservationDate: date

    def __init__(self, user: User, reservedItem: BookItem, reservationDate: date):
        self._user = user
        self._reservedItem = reservedItem
        self._reservationDate = reservationDate

    def getItem(self) -> BookItem:
        return self._reservedItem

    def getUser(self) -> User:
        return self._user
    
    def __str__(self) -> str:
        library = lib.Library.getLibrary()
        book = library.getBookById(self._reservedItem.getBookId())
        title = book.getTitle()
        return f"- Título: {title}\n \t- Data do reserva: {self._reservationDate}"
