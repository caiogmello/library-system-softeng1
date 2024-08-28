from abc import ABC, abstractmethod

class Loan(ABC):
    @abstractmethod
    def exec(self, user: "User", bookId: int) -> None:
        """
        Try to loan a book from the library.
        Print error message in case of failure.
        """
        pass

