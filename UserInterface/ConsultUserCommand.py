from UserInterface.LibraryCommand import LibraryCommand
import Library.Library as lib

class ConsultUserCommand(LibraryCommand):
    def exec(self, userId: int) -> None:
        library = lib.Library.getLibrary()
        user = library.getUserById(userId)

        if user is None:
            print(f"Usuário com ID {userId} não encontrado.")
            return

        loans = library.allLoansPerUser(user)
        reservations = library.allReservationsPerUser(user)
        loanInfo = f"Empréstimos:" + "\n".join(
            [f"  - {loan.getItem().getTitle()} - {loan.getItem().getId()}" for loan in loans]
        )
        reservationInfo = f"Reservas:" + "\n".join(
            [f"  - {reservation.getItem().getTitle()} - {reservation.getItem().getId()}" for reservation in reservations]
        )
        print(f"Usuário: {user.name}\n{loanInfo}\n{reservationInfo}")
        return super().exec()
