from datetime import datetime

class Book:

    _id: int 
    _exampleId: int 
    _title: str 
    _publisher: str 
    _authors: list[str] 
    _edition: str 
    _year: datetime 
    
    
    def __init__(self, bookId: int, exampleId: int,
                 title: str, publisher: str, authors: list[str],
                  edition: str, year: datetime) -> None:
        
        self._id = bookId
        self._exampleId = exampleId
        self._title = title
        self._publisher = publisher
        self._authors= authors
        self._edition = edition
        self._year = year
    
    def getId(self) -> int:
        return self._id
    
    def getExampleId(self) -> int:
        return self._exampleId
    
    def getTitle(self) -> str:
        return self._title
    
    def getPublisher(self) -> str:
        return self._publisher
    
    def getAuthors(self) -> list[str]:
        return self._authors
    
    def getEdition(self) -> str:
        return self._edition
    
    def getYear(self) -> datetime:
        return self._year
    
    def __str__(self) -> str:
        return f"""
            Book ID: {self._id}
            Example ID: {self._exampleId}
            Title: {self._title}
            Publisher: {self._publisher}
            Authors: {self._authors}
            Edition: {self._edition}
            Year: {self._year}
        """