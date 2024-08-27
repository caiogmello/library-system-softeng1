from Book.Book import Book
from datetime import datetime

class Factory:

    @staticmethod
    def createBook(bookId: int, exampleId: int,
                   title: str, publisher: str, authors: list[str],
                   edition: str, year: datetime) -> Book:
        return Book(bookId, exampleId, title, publisher, authors, edition, year)
    
    @staticmethod
    def createBookFromDict(bookDict: dict) -> Book:
        return Factory.createBook(
            bookDict["bookId"],
            bookDict["exampleId"],
            bookDict["title"],
            bookDict["publisher"],
            bookDict["authors"],
            bookDict["edition"],
            bookDict["year"]
        )
    