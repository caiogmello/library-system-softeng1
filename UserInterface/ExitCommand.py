from UserInterface.LibraryCommand import LibraryCommand

class ExitCommand(LibraryCommand):
    def exec(self) -> None:
        exit(0)

