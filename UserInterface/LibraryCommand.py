from abc import abstractmethod, ABC

class LibraryCommand(ABC):
    @abstractmethod
    def exec(self) -> None:
        """
        Execute command issued.
        """
        pass
