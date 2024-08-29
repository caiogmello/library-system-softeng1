from UserInterface.LibraryCommand import LibraryCommand

import Library.Library as lib

class CountNotificationsCommand(LibraryCommand):
    def exec(self, userId: int) -> None:
        library = lib.Library.getLibrary()
        user = library.getUserById(userId)
        if user is None:
            print(f"Usuário com ID {userId} não encontrado.")

        print(f"O usuário {user.name} tem {user.getNotificationCount()} notificações sobre reservas duplicadas.")
        return super().exec()

