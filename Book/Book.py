from Book.BookItem import BookItem
from Observer.Subject import Subject

class Book(Subject):
    _id: str 
    _title: str 
    _publisher: str 
    _authors: list[str] 
    _edition: str 
    _year: str 
    _copies: list[BookItem]
    _reserved: list[BookItem]
    _loaned: list[BookItem]
    
    def __init__(self, bookId: str, title: str, publisher: str,
                  authors: list[str], edition: str, year: str) -> None:
        
        self._id = bookId
        self._title = title
        self._publisher = publisher
        self._authors= authors
        self._edition = edition
        self._year = year
        self._copies = []
        self._reserved = []
        self._loaned = []
        self.observers = []
    
    def getId(self) -> str:
        return self._id
    
    def getTitle(self) -> str:
        return self._title
    
    def getPublisher(self) -> str:
        return self._publisher
    
    def getAuthors(self) -> list[str]:
        return self._authors
    
    def getEdition(self) -> str:
        return self._edition
    
    def getYear(self) -> str:
        return self._year

    def getCopies(self) -> list[BookItem]:
        return self._copies

    def addCopy(self, copyId: int) -> None:
        self._copies.append(BookItem(copyId, self._id))

    def findCopyById(self, copyId: int) -> BookItem | None:
        for copy in self._copies:
            if copy.getId() == copyId:
                return copy
        return None

    def removeCopyById(self, copyId: int) -> None:
        item = self.findCopyById(copyId)
        if item is not None:
            self._copies.remove(item)
    
    def removeAnyCopy(self) -> BookItem:
        if len(self._copies) > 0:
            return self._copies.pop()
        else:
            return None
        
    def getAnyCopy(self) -> BookItem:
        if len(self._copies) > 0:
            return self._copies[-1]
        else:
            return None
    
    def reserveAnyCopy(self) -> BookItem:
        copy = self.getAnyCopy()
        if copy is None:
            raise Exception(f"Nenhuma cópia de livro ID={self._id} disponível para reserva")
        self._reserved.append(copy)
        
        # notify of duplicate reservations
        if len(self._reserved) > 1:
            self.notifyObservers()
        return copy

    def loanAnyCopy(self) -> BookItem:
        copy = self.removeAnyCopy()
        if copy is None:
            raise Exception(f"Nenhuma cópia de livro ID={self._id} disponível para empréstimo")
        self._loaned.append(copy)
        return copy

    def returnReservedCopy(self, copy: BookItem) -> None:
        self._reserved.remove(copy)
        self._copies.append(copy)

    def returnLoanedCopy(self, copy: BookItem) -> None:
        self._loaned.remove(copy)
        self._copies.append(copy)

    def __str__(self) -> str:
        return f"""
            Book ID: {self._id}
            Title: {self._title}
            Publisher: {self._publisher}
            Authors: {self._authors}
            Edition: {self._edition}
            Year: {self._year}
        """
