from User.UserState import UserState
from Operation.Exception import OperationException

class UserIndebted(UserState):
    def loanBook(self, user: 'User', bookId: int) -> None:
        raise OperationException(
            operationType=user.loanOperation,
            user=user,
            bookId=bookId,
            reason="Usuário está em débito",
        )