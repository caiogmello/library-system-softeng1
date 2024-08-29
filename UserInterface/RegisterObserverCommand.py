from UserInterface.LibraryCommand import LibraryCommand
import Library.Library as lib

class RegisterObserverCommand(LibraryCommand):
    def exec(self, userId: int, bookId: int) -> None:
        library = lib.Library.getLibrary()

        user = library.getUserById(userId)
        if user is None:
            print(f"Usuário com ID {userId} não encontrado.")
            return

        book = library.getBookById(bookId)
        if book is None:
            print(f"Livro com ID {bookId} não encontrado.")
            return

        book.registerObserver(user)
        return super().exec()
