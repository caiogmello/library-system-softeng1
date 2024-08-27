from datetime import date

from Book.BookItem import BookItem
from User.User import User

class LoanItem:
    _user: User
    _loanedItem: BookItem
    _loanDate: date
    _devolutionDate: date

    def __init__(
        self,
        user: User,
        loanedItem: BookItem,
        loanDate: date,
        devolutionDate: date
    ):
        self._user = user
        self._loanedItem = loanedItem
        self._loanDate = loanDate
        self._devolutionDate = devolutionDate

    def getItem(self) -> BookItem:
        return self._loanedItem

    def getUser(self) -> User:
        return self._user

    def getLoanDate(self) -> date:
        return self._loanDate

    def getDevolutionDate(self) -> date:
        return self._devolutionDate
