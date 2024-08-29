from abc import abstractmethod, ABC

class LibraryCommand(ABC):
    @abstractmethod
    def exec(self, *args) -> None:
        """
        Execute command issued.
        """
        pass
