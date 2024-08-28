from User.UserState import UserState

class UserNotIndebted(UserState):
    def loanBook(self, user: "User", bookId: int) -> None:
        """
        Try to loan a book from the library.
        Print error message in case of failure.
        """
        user.loanOperation.exec(user, bookId)
