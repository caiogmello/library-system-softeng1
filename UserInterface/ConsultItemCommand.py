from UserInterface.LibraryCommand import LibraryCommand
import Library.Library as lib

class ConsultItemCommand(LibraryCommand):
    def exec(self, bookId: int) -> None:
        library = lib.Library.getLibrary()
        book = library.getBookById(bookId)

        if book is None:
            print(f"Livro com ID {bookId} não encontrado.")
            return
        
        title = book.getTitle()
        copies = book.getCopies()
        reservations = library.getReservations(bookId)
        users = f"{', '.join([item.getUser().name for item in reservations])}"

        print(f"""
            Título: {title}
            Reservas: {len(reservations)}
            """)            
        if len(reservations) > 0:
            print(f"""
            Usuários com reserva: {users}
            """)
        for cop in copies:
            print(library.getBookInfo(bookId, cop.getId()))

        return super().exec()
