from datetime import datetime

class Book:
    def __init__(self, book_id: int, example_id: int,
                 title: str, publisher: str, authors: list[str],
                  edition: str, year: datetime) -> None:
        self._book_id: int = book_id
        self._example_id: int = example_id
        self._title: str = title
        self._publisher: str = publisher
        self._authors: list[str] = authors
        self._edition: str = edition
        self._year: datetime = year
    
    def getBookId(self) -> int:
        return self._book_id
    
    def getExampleId(self) -> int:
        return self._example_id
    
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
            Book ID: {self._book_id}
            Example ID: {self._example_id}
            Title: {self._title}
            Publisher: {self._publisher}
            Authors: {self._authors}
            Edition: {self._edition}
            Year: {self._year}
        """