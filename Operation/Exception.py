from Operation.Operation import Operation

class OperationException(Exception):

    _operationsDict: dict[str, str] = {}

    def __init__(
        self,
        operationType: Operation,
        user: 'User',
        bookId: int,
        reason: str,
    ):
        self._operationsDict["StudentLoan"]  = self._operationsDict["ProfessorLoan"] = self._operationsDict["Loan"] = "empréstimo"
        self._operationsDict["Reservation"] = "reserva"
        self._operationsDict["Devolution"] = "devolução"
        self._operationsDict["CancelReservationIfExists"] = "cancelamento de reserva"
    

        self.message = (
            f"Operação de {self._operationsDict[operationType.__name__]} não pôde ser realizada para o usuário {user.name}"
            f" e livro com ID {bookId} pelo seguinte motivo: \n\t- {reason}"
        )
        super().__init__(self.message)

    def __str__(self):
        return self.message
