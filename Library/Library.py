from typing import Union
from datetime import date, timedelta

from User.User import User
from Book.Book import Book
from Operation.Operation import Operation
from UserInterface.Factory import Factory
from Library.LoanItem import LoanItem
from Library.ReservationItem import ReservationItem

class Library:
    _instance: Union["Library", None] = None
    _books: list[Book] = []
    _operations: list[Operation] = [] # operations performed in the library
    _reservations: dict[int, list[ReservationItem]] = {} # bookId -> reservations
    _loans: dict[int, list[LoanItem]] = {} # bookId -> loans

    @staticmethod
    def getLibrary() -> "Library":
        if Library._instance is None:
            Library._instance = Library()
        return Library._instance
    
    def __init__(self):
        pass

    def getBookById(self, bookId: int) -> Union[Book, None]:
        for book in self._books:
            if book.getId() == bookId:
                return book
        return None

    def addBook(self, book: Book, copyId: int) -> None:
        """
        if the copy is already in the library, it will not be added again
        """
        libraryBook = self.getBookById(book.getId())
        if libraryBook is None:
            self._books.append(book)
            libraryBook = book
        libraryBook.addCopy(copyId)

    def addBookByDict(self, bookDict: dict) -> None:
        book = Factory.createBookFromDict(bookDict)
        self.addBook(book)
    
    def removeBook(self, book: Union[Book, None], copyId: int) -> bool:
        libraryBook = self.getBookById(book.getId())
        if libraryBook is None:
            return False
        libraryBook.removeCopyById(copyId)
    
    def reserveBook(self, user: User, bookId: int) -> None:
        book = self.getBookById(bookId)
        if book is None:
            raise Exception(f"Livro ID={bookId} não encontrado.")
        copy = book.reserveAnyCopy()
        if bookId not in self._reservations.keys():
            self._reservations[bookId] = []
        self._reservations[bookId].append(ReservationItem(user, copy))
    
    # def unreserveBook(self, user: User, book: Book) -> bool:
    #     if book.getId() not in self._reservations.keys():
    #         return False
        
    #     if user not in self._reservations[book.getId()]:
    #         return False
        
    #     self._reservations[book.getId()].remove(user)
    #     return True

    def loanBook(self, user: User, bookId: int, loanTimeDays: int):
        book = self.getBookById(bookId)
        if book is None:
            raise Exception(f"Livro ID={bookId} não encontrado.")
        copy = book.loanAnyCopy()
        if bookId not in self._loans.keys():
            self._loans[bookId] = []
        self._loans[bookId].append(LoanItem(user, copy, date.today(), date.today() + timedelta(days=loanTimeDays)))
        return True

    def getReservations(self, bookId: int) -> list[ReservationItem]:
        if bookId not in self._reservations.keys():
            return []
        return self._reservations[bookId]

    def findReservation(self, bookId: int, copyId: int) -> ReservationItem | None:
        if bookId not in self._reservations.keys():
            return None
        for reservation in self._reservations[bookId]:
            if reservation.getItem().getId() == copyId:
                return reservation
        return None

    def findLoan(self, bookId: int, copyId: int) -> LoanItem | None:
        if bookId not in self._loans.keys():
            return None
        for loan in self._loans[bookId]:
            if loan.getCopy().getItem().getId() == copyId:
                return loan
        return None
    
    def getItemInfo(self, bookId: int, copyId: int) -> str:
        book = self.getBookById(bookId)
        if book is None:
            return f"Copy {copyId} not found."

        copy = book.findCopyById(copyId)
        reservation = self.findReservation(bookId, copyId)
        loan = self.findLoan(bookId, copyId)

        copyInfo = f"Exemplar: {copyId}"

        if copy:
            statusInfo = "   - Status: Disponível."
        if copy is None and reservation:
            statusInfo = (
                f""""
                - Status: Reservado.
                Informações da reserva:
                - Usuário: {reservation.getUser().name}
                """
            )
        elif copy is None and loan:
            statusInfo = ( 
                f""""
                - Status: Emprestado.
                Informações do empréstimo:	
                - Usuário: {loan.getUser().name}
                - Data de empréstimo: {loan.getLoanDate()}
                - Data prevista de devolução: {loan.getDevolutionDate()}
                """   
            )
        else:
            statusInfo = "   - Status: Indisponível."
        return "\n".join([copyInfo, statusInfo])
    