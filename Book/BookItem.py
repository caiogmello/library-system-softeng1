class BookItem:
    """id of the book item"""
    _copyId: str 
    _bookId: str

    def __init__(self, id: str, bookId: str) -> None:
        self._copyId = id
        self._bookId = bookId
    
    def getId(self) -> str:
        return self._copyId
    
    def getBookId(self) -> str:
        return self._bookId
