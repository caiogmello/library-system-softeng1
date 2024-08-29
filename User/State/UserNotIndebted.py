from User.State.UserState import UserState

class UserNotIndebted(UserState):
    def loanBook(self, user: "User", bookId: int) -> 'BookItem':
        """
        Try to loan a book from the library.
        Print error message in case of failure.
        """
        return user.loanOperation.exec(user, bookId)
