from UserInterface.LibraryCommand import LibraryCommand

class ExitCommand(LibraryCommand):
    def exec(self) -> None:
        print("Finalizando o programa.")
        exit(0)

