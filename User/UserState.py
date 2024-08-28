from abc import ABC, abstractmethod

from Book.BookItem import BookItem

class UserState(ABC):
    @abstractmethod
    def loanBook(self, user: 'User', bookId: int) -> BookItem:
        pass
