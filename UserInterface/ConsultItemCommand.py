from UserInterface.LibraryCommand import LibraryCommand
import Library.Library as lib

class ConsultItemCommand(LibraryCommand):
    def exec(self, bookId: int) -> None:
        library = lib.Library.getLibrary()
        # TODO implement this
        book = library.getBookById(bookId)

        if book is None:
            print("Nenhum livro encontrado com ID " + str(bookId))
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
            print(library.getItemInfo(bookId, cop.getId()))

        return super().exec()
