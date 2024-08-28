from UserInterface.LibraryCommand import LibraryCommand
import Library.Library as lib

class ReturnItemCommand(LibraryCommand):
    def exec(self, userId: int, bookId: int) -> None:
        library = lib.Library.getLibrary()
        user = library.getUserById(userId)
        book = library.getBookById(bookId)  

        if user is None:
            print(f"Usuário com ID {userId} não encontrado.")
            return
        
        if book is None:
            print(f"Livro com ID {bookId} não encontrado.")
            return
    
        user.returnBook(bookId)
        return super().exec()