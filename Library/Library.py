from typing import Union
from datetime import date, timedelta

import User.User as user
from Book.Book import Book
from Book.BookItem import BookItem
from Operation.Operation import Operation
from UserInterface.Factory import Factory
from Library.LoanItem import LoanItem
from Library.ReservationItem import ReservationItem

class Library:
    _instance: Union["Library", None] = None
    _books: list[Book] = []
    _operations: list[Operation] = [] # operations performed in the library
    _historicReservations: dict[int, list[ReservationItem]] = {} # bookId -> reservations
    _historicLoans: dict[int, list[ReservationItem]] = {} # bookId -> reservations
    _reservations: dict[int, list[ReservationItem]] = {} # bookId -> reservations
    _loans: dict[int, list[LoanItem]] = {} # bookId -> loans
    _users: list[user.User] = []    

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
        self.addBook(book, bookDict["copyId"])
    
    def removeBook(self, book: Union[Book, None], copyId: int) -> bool:
        libraryBook = self.getBookById(book.getId())
        if libraryBook is None:
            return False
        libraryBook.removeCopyById(copyId)
    
    def reserveBook(self, user: user.User, bookId: int) -> BookItem:
        book = self.getBookById(bookId)
        if book is None:
            raise Exception(f"Livro ID={bookId} não encontrado.")
        copy = book.reserveAnyCopy()
        if bookId not in self._reservations.keys():
            self._reservations[bookId] = []
        if bookId not in self._historicReservations.keys():
            self._historicReservations[bookId] = []

        if self.isReservedByUser(bookId, user):
            raise Exception(f"Usuário {user.name} já possui uma reserva para o livro ID={book.getId()}.")	
        self._reservations[bookId].append(ReservationItem(user, copy))
        self._historicReservations[bookId].append(ReservationItem(user, copy))
        return copy
    
    def isReservedByUser(self, bookId: int, user: user.User) -> bool:
        if bookId not in self._reservations.keys():
            return False
        for reservation in self._reservations[bookId]:
            if reservation.getUser() == user:
                return True
        return False
    
    def unreserveBook(self, user: user.User, bookId: int) -> BookItem:
        book = self.getBookById(bookId)
        if book is None:
            raise Exception(f"Livro ID={bookId} não encontrado.")

        if bookId not in self._reservations.keys():
            raise Exception(f"Livro ID={bookId} não está reservado por nenhum usuário.")

        reservation = None
        for registeredReservation in self._reservations[bookId]:
            if registeredReservation.getUser() == user:
                reservation = registeredReservation
                break
        if reservation is None:
            raise Exception(f"Livro ID={bookId} não está reservado por {user.name}.")

        copy = reservation.getItem()
        book.returnReservedCopy(copy)
        self._reservations[bookId].remove(reservation)

        return copy
    
    def returnBook(self, user: user.User, bookId: int) -> None:
        book = self.getBookById(bookId)
        if book is None:
            raise Exception(f"Livro ID={bookId} não encontrado.")

        if bookId not in self._loans:
            raise Exception(f"Livro ID={bookId} não está emprestado.")

        loan = None
        for registeredLoan in self._loans[bookId]:
            if registeredLoan.getUser() == user:
                loan = registeredLoan
                break
        if loan is None:
            raise Exception(f"Usuário {user.name} não possui empréstimo do livro ID={bookId}.")
        copy = loan.getItem()
        book.returnLoanedCopy(copy)
        self._loans[bookId].remove(loan)

    def loanBook(self, user: user.User, bookId: int) -> BookItem:
        book = self.getBookById(bookId)
        if book is None:
            raise Exception(f"Livro ID={bookId} não encontrado.")
        copy = book.loanAnyCopy()
        if bookId not in self._loans.keys():
            self._loans[bookId] = []
        if bookId not in self._historicLoans.keys():
            self._historicLoans[bookId] = []

        self._loans[bookId].append(LoanItem(user, copy, date.today(), date.today() + timedelta(days=user.maxLoanTimeDays)))
        self._historicLoans[bookId].append(LoanItem(user, copy, date.today(), date.today() + timedelta(days=user.maxLoanTimeDays)))
        return copy

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
            if loan.getItem().getId() == copyId:
                return loan
        return None
    
    def getBookInfo(self, bookId: int, copyId) -> str:
        book = self.getBookById(bookId)
        if book is None:
            return f"Copy {copyId} not found."

        copy = book.findCopyById(copyId)
        reservation = self.findReservation(bookId, copyId)
        loan = self.findLoan(bookId, copyId)

        copyInfo = f"\tExemplar: {copyId}"


        if copy:
            statusInfo = "\t- Status: Disponível.\n" 

        if self.findLoan(bookId, copyId):
            statusInfo = ( 
                f"""\t- Status: Emprestado.
\t\tInformações do empréstimo:	
\t\t- Usuário: {loan.getUser().name}
\t\t- Data de empréstimo: {loan.getLoanDate()}
\t\t- Data prevista de devolução: {loan.getDevolutionDate()}
                """   
            )

        return "\n".join([copyInfo, statusInfo])
    
    def addUser(self, user: user.User) -> bool:
        if user not in self._users:
            self._users.append(user)
            return True
        return False
    
    def getUserById(self, userId: int) -> user.User | None:
        for user in self._users:
            if user.id == userId:
                return user
        return None

    def allLoansPerUser(self, user: user.User) -> list[LoanItem]:
        loans = []
        for loan in self._historicLoans:
            if loan.getUser() == user:
                loans.append(loan)
        return loans

    def allReservationsPerUser(self, user: user.User) -> list[ReservationItem]:
        reservations = []
        for reservation in self._historicReservations:
            if reservation.getUser() == user:
                reservations.append(reservation)
        return reservations
