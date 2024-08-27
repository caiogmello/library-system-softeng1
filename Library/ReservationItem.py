from Book.BookItem import BookItem
from User.User import User

class ReservationItem:
    _user: User
    _reservedItem: BookItem

    def __init__(self, user: User, reservedItem: BookItem):
        self._user = user
        self._reservedItem = reservedItem

    def getItem(self) -> BookItem:
        return self._loanedItem

    def getUser(self) -> User:
        return self._user
