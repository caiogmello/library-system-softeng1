from Operation.Operation import Operation
from User.User import User
from Book.Book import Book

class OperationException(Exception):
    def __init__(
        self,
        operationType: Operation,
        user: User,
        item: Book,
        reason: str,
    ):
        self.message = (
            f"Operação '{operationType}' não pôde ser realizada para o usuário '{user.name}'"
            f" e livro '{item.id}' pelo seguinte motivo: '{reason}'"
        )
        super().__init__(self.message)
