from UserInterface.LibraryCommand import LibraryCommand

class Console:
    _instance: "Console" | None = None
    commands: dict[str, LibraryCommand] = {}

    @staticmethod
    def getConsole() -> "Console":
        if Console._instance is None:
            Console._instance = Console()
        return Console._instance

    def initCommands(self) -> None:
        pass

    def __init__(self):
        self.initCommands()

    def service(self) -> None:
        pass
