
class Book:

    _id: str 
    _copyId: str 
    _title: str 
    _publisher: str 
    _authors: list[str] 
    _edition: str 
    _year: str 
    
    
    def __init__(self, bookId: str, copyId: str,
                 title: str, publisher: str, authors: list[str],
                  edition: str, year: str) -> None:
        
        self._id = bookId
        self._copyId = copyId
        self._title = title
        self._publisher = publisher
        self._authors= authors
        self._edition = edition
        self._year = year
    
    def getId(self) -> str:
        return self._id
    
    def getCopyId(self) -> str:
        return self._copyId
    
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