from Console.Command.LibraryCommand import LibraryCommand
from Observer.Observer import Observer
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

        try:
            if isinstance(user, Observer):
                book.registerObserver(user)
                print(f"Usuário {user.name} registrado como observador do livro {book.getTitle()}.")
            else:
                print(f"Usuário {user.name} não pode ser registrado como observador.")
        except Exception as e:
            print(f"Erro ao registrar observador: {e}")
        return super().exec()
