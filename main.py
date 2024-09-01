from Console.Console import Console
from Library.Library import Library
from Console.Data import getBooks, getUsers


if __name__ == "__main__":
    lib: Library = Library.getLibrary()

    books = getBooks()
    users = getUsers()

    for book in books:
        lib.addBookByDict(book)
    for user in users:
        lib.addUser(user)

    console = Console.getConsole()
    console.service()
    