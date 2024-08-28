from UserInterface.Console import Console
from Library.Library import Library
from UserInterface.Data import getBooks, getUsers


if __name__ == "__main__":
    lib: Library = Library.getLibrary()

    books = getBooks()
    users = getUsers()

    for book in books:
        lib.addBookByDict(book)

    lib.reserveBook(users[0], "100")
    lib.reserveBook(users[1], "100")
    # lib.reserveBook(users[2], "102")

    console = Console.getConsole()
    console.service()
    