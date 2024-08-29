from datetime import date

from Book.BookItem import BookItem
from User.User import User
import Library.Library as lib

class LoanItem:
    _user: User
    _loanedItem: BookItem
    _loanDate: date
    _devolutionDate: date
    _status: str

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
        self._status = "Em curso"

    def getItem(self) -> BookItem:
        return self._loanedItem

    def getUser(self) -> User:
        return self._user

    def getLoanDate(self) -> date:
        return self._loanDate

    def getDevolutionDate(self) -> date:
        return self._devolutionDate
    
    def closeLoan(self) -> None:
        self._status = "Fechado"

    def isClosed(self) -> bool:
        return self._status == "Fechado"
    
    def openLoan(self) -> None:
        self._status = "Em curso"

    def __str__(self) -> str:
        library = lib.Library.getLibrary()
        book = library.getBookById(self._loanedItem.getBookId())
        title = book.getTitle()
        devolutionDateLabel = "Data de devolução" if self._status == "Fechado" else "Data prevista de devolução"	
        return f"- Título: {title}\n \t- Data do empréstimo: {self._loanDate}\n\t- Status: {self._status}\n\t- {devolutionDateLabel}: {self._devolutionDate}"