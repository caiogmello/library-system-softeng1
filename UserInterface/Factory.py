from Book.Book import Book

class Factory:

    @staticmethod
    def createBook(bookId: int, 
                   title: str, publisher: str, authors: list[str],
                   edition: str, year: str) -> Book:
        
        return Book(bookId, title, publisher, authors, edition, year)
    
    @staticmethod
    def createBookFromDict(bookDict: dict) -> Book:
        return Factory.createBook(
            bookDict["id"],
            bookDict["title"],
            bookDict["publisher"],
            bookDict["authors"],
            bookDict["edition"],
            bookDict["year"]
        )
    
