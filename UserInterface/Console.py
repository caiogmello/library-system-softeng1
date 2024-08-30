from typing import Union

from UserInterface.LibraryCommand import LibraryCommand
from UserInterface.ConsultItemCommand import ConsultItemCommand
from UserInterface.ConsultUserCommand import ConsultUserCommand
from UserInterface.CountNotificationsCommand import CountNotificationsCommand
from UserInterface.RegisterObserverCommand import RegisterObserverCommand
from UserInterface.ExitCommand import ExitCommand
from UserInterface.LoanItemCommand import LoanItemCommand
from UserInterface.ReserveItemCommand import ReserveItemCommand
from UserInterface.ReturnItemCommand import ReturnItemCommand
class Console:
    _instance: Union["Console", None] = None
    commands: dict[str, LibraryCommand] = {}
    numArgs: dict[str, int] = {}

    @staticmethod
    def getConsole() -> "Console":
        if Console._instance is None:
            Console._instance = Console()
        return Console._instance

    def initCommands(self) -> None:
        self.commands["emp"] = LoanItemCommand()
        self.commands["dev"] = ReturnItemCommand()
        self.commands["res"] = ReserveItemCommand()
        self.commands["obs"] = RegisterObserverCommand()
        self.commands["liv"] = ConsultItemCommand()
        self.commands["usu"] = ConsultUserCommand()
        self.commands["ntf"] = CountNotificationsCommand()
        self.commands["sai"] = ExitCommand()

        self.numArgs["emp"] = self.numArgs["dev"] = self.numArgs["res"] = self.numArgs["obs"] = 2
        self.numArgs["liv"] = self.numArgs["usu"] = self.numArgs["ntf"] = 1
        self.numArgs["sai"] = 0

    def __init__(self):
        self.initCommands()

    def service(self) -> None:
        while True:
            options = input("Execute um comando: ").split()
            command = options[0]
            if command not in self.commands:
                print(f"Comando inválido: esperado um dentre {', '.join(self.commands.keys())}")
            elif len(options) - 1 == self.numArgs[command]:
                self.commands[command].exec(*options[1:])
            else:
                print(f"Comando {command} esperava {self.numArgs[command]} argumentos, mas recebeu {len(options) - 1}.")
