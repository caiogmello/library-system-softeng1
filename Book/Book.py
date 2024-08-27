from Book.BookItem import BookItem

class Book:
    _id: str 
    _title: str 
    _publisher: str 
    _authors: list[str] 
    _edition: str 
    _year: str 
    _copies: list[BookItem]
    
    def __init__(self, bookId: str, title: str, publisher: str, authors: list[str],
                  edition: str, year: str) -> None:
        
        self._id = bookId
        self._title = title
        self._publisher = publisher
        self._authors= authors
        self._edition = edition
        self._year = year
        self._copies = []
    
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
        self._copies.append(BookItem(copyId))

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

    def __str__(self) -> str:
        return f"""
            Book ID: {self._id}
            Copy ID: {self._copyId}
            Title: {self._title}
            Publisher: {self._publisher}
            Authors: {self._authors}
            Edition: {self._edition}
            Year: {self._year}
        """
