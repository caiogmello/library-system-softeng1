from Operation.Operation import Operation

class OperationException(Exception):
    def __init__(
        self,
        operationType: Operation,
        user: 'User',
        bookId: int,
        reason: str,
    ):
        self.message = (
            f"Operação de '{operationType.__name__}' não pôde ser realizada para o usuário '{user.name}'"
            f" e livro '{bookId}' pelo seguinte motivo: '{reason}'"
        )
        super().__init__(self.message)

    def __str__(self):
        return self.message
