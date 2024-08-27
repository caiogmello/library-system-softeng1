from User.User import User
from Book.Book import Book
from Operation.Operation import Operation
from typing import Union
from UserInterface.Factory import Factory
from collections import deque
class Library:
    _instance: Union["Library", None] = None
    _books: dict[Book, bool] = {} # book (copy) -> isAvailable
    """
    copyId is unique, bookId not necessarily
    """
    _copies: dict[int, list[Book]] = {} # bookId -> list of available copies
    _operations: list[Operation] = [] # operations performed in the library
    _reservedBooks: dict[Book, User] = {} # reserved book -> user

    @staticmethod
    def getLibrary() -> "Library":
        if Library._instance is None:
            Library._instance = Library()
        return Library._instance
    
    def __init__(self):
        pass

    def addBook(self, book: Book) -> None:
        """
        if the copy is already in the library, it will not be added again
        """
        if self.getBookByCopyId(book.getCopyId()) is not None:
            book = self.getBookByCopyId(book.getCopyId())
            if self._books[book]:
                return
            
        self._books[book] = True
        if book.getId() not in self._copies.keys():
            self._copies[book.getId()] = []
        self._copies[book.getId()].append(book)

    def addBookByDict(self, bookDict: dict) -> None:
        book = Factory.createBookFromDict(bookDict)
        self.addBook(book)
    
    def removeBook(self, book: Union[Book, None]) -> bool:
        if book is not None and self._books[book]:
            self._books[book] = False
            self._copies[book.getId()].remove(book)
            return True
        return False
    
    def getBookById(self, bookId: int) -> Union[Book, None]:
        if bookId in self._copies.keys() and len(self._copies[bookId]) > 0:
            return self._copies[bookId][0]
   
        return None
    
    def getBookByCopyId(self, copyId: int) -> Union[Book, None]:
        for book in self._books.keys():
            if book.getCopyId() == copyId:
                return book
        return None
    
    def getAvailableBooks(self) -> list[Book]:
        return [book for book in self._books if self._books[book]]
    
    def getUnavailableBooks(self) -> list[Book]:
        return [book for book in self._books if not self._books[book]]
    
    def getAvailableBookCopies(self, book: Union[Book, None]) -> int:
        if book is None:
            return 0
        return len(self._copies[book.getId()])
    
    def getTotalBookCopies(self, book: Union[Book, None]) -> int:
        if book is None:
            return 0
        return sum([1 for b in self._books.keys() if b.getId() == book.getId()])
        