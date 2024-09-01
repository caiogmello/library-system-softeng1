from Console.Command.LibraryCommand import LibraryCommand
import Library.Library as lib

class ConsultUserCommand(LibraryCommand):
    def exec(self, userId: int) -> None:
        library = lib.Library.getLibrary()
        user = library.getUserById(userId)

        if user is None:
            print(f"Usuário com ID {userId} não encontrado.")
            return super().exec()

        loans = library.allLoansPerUser(user)
        reservations = library.allReservationsPerUser(user)
        loanInfo = f"\tEmpréstimos:\n" + "\n".join(
            [f"\t{loan}" for loan in loans]
        )
        reservationInfo = f"\tReservas:\n" + "\n".join(
            [f"\t{reservation}" for reservation in reservations]
        )
        print(f"Usuário: {user.name}\n{loanInfo}\n{reservationInfo}")
        return super().exec()
