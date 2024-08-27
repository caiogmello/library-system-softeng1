from UserInterface.Console import Console
from UserInterface.Factory import Factory
from User.Professor import Professor
from Library.Library import Library

if __name__ == "__main__":
    # console = Console.getConsole()
    # console.service()
    lib: Library = Library.getLibrary()
    book1 = {
        "id": "1",
        "copyId": "21",
        "title": "Author1",
        "publisher": "Publisher",
        "authors": ["Author1"],
        "edition": "1",
        "year": "2021"
    }
    book2 = {
        "id": "31",
        "copyId": "23",
        "title": "Author2",
        "publisher": "Publisher1",
        "authors": ["Author1", "Author2"],
        "edition": "3",
        "year": "2020"
    }
    book3 = {
        "id": "31",
        "copyId": "24",
        "title": "Author2",
        "publisher": "Publisher1",
        "authors": ["Author1", "Author2"],
        "edition": "3",
        "year": "2020"
    }

    lib.addBookByDict(book1)
    lib.addBookByDict(book2)
    lib.removeBook(lib.getBookById("3"))
    lib.addBookByDict(book3)
    lib.addBookByDict(book3)
    lib.removeBook(lib.getBookById(book3["id"]))


    print("Available books")	
    for l in lib.getAvailableBooks():
        print(l)

    print("Unavailable books")
    for l in lib.getUnavailableBooks():
        print(l)

    id = "31"
    print(f"Available copies w id {id}")
    print(lib.getAvailableBookCopies(lib.getBookById(id)))

    print(f"Total copies w id {id}")
    print(lib.getTotalBookCopies(lib.getBookById(id)))
    