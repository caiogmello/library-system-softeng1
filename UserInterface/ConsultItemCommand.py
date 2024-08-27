from UserInterface.LibraryCommand import LibraryCommand
from Library.Library import Library 
from Book.Book import Book
class ConsultItemCommand(LibraryCommand):
    def exec(self, bookId: int, library: Library) -> None:
        # TODO implement this
        book = library.getBookById(bookId)

        if book is None:
            print("No book found with id " + str(bookId))
            return
        
        title = book.getTitle()
        reservations = library.getReservations(book)
        copies: list[Book] = library.getTotalBookCopies(book)
        users = f"{', '.join([user.name for user in reservations])}"

        print(f"""
            Título: {title}
            Reservas: {len(reservations)}
            """)            
        if len(reservations) > 0:
            print(f"""
            Usuários com reserva: {users}
            """)
        for cop in copies:
            print(f"Exemplar: {cop.getCopyId()}")
            print(library.getCopyInfo(cop.getCopyId()))

        return super().exec()
