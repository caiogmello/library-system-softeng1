from abc import ABC, abstractmethod

class UserState(ABC):
    @abstractmethod
    def loanBook(self, user: 'User', bookId: int) -> None:
        pass
