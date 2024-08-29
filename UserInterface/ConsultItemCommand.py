from UserInterface.LibraryCommand import LibraryCommand
import Library.Library as lib

class ConsultItemCommand(LibraryCommand):
    def exec(self, bookId: int) -> None:
        library = lib.Library.getLibrary()
        book = library.getBookById(bookId)

        if book is None:
            print(f"Livro com ID {bookId} não encontrado.")
            return
        
        # TODO: não sei se tá certo a gente acessar métodos de book direto, talvez
        # só a biblioteca q deveria fazer isso
        title = book.getTitle()
        copies = book.getCopies()
        reservations = library.getReservations(bookId)
        users = "\n\t- " +  "\n\t- ".join([item.getUser().name for item in reservations])

        print(f"""
Título: {title}
\tReservas: {len(reservations)}
""")            
        if len(reservations) > 0:
            print(f"""
\tUsuários com reserva: {users}
""")
        for cop in copies:
            print(library.getBookInfo(bookId, cop.getId()))

        return super().exec()
