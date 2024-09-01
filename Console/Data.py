from User.PostgraduateStudent import PostgraduateStudent
from User.UndegraduateStudent import UndegraduateStudent
from User.Professor import Professor

def getBooks():
    return [{
        "id": "100",
        "copyId": "01",
        "title": "Engenharia de Software",
        "publisher": "AddisonWesley",
        "authors": ["Ian Sommerville"],
        "edition": "6ª",
        "year": "2000"
    },{
        "id": "100",
        "copyId": "02",
        "title": "Engenharia de Software",
        "publisher": "AddisonWesley",
        "authors": ["Ian Sommerville"],
        "edition": "6ª",
        "year": "2000"
    }, {
        "id": "101",
        "copyId": "03",
        "title": "UML - Guia do Usuário",
        "publisher": "Campus",
        "authors": ["Grady Booch", "James Rumbaugh", "Ivar Jacobson"],
        "edition": "7ª",
        "year": "2000"
    }, {
        "id": "200",
        "copyId": "04",
        "title": "Code Complete",
        "publisher": "Microsoft Press",
        "authors": ["Steve McConnell"],
        "edition": "2ª",
        "year": "2014"
    }, {
        "id": "201",
        "copyId": "05",
        "title": "Agile Software Development, Principles, Patterns, and Practices",
        "publisher": "Prentice Hall",
        "authors": ["Robert Martin"],
        "edition": "1ª",
        "year": "2002"
    }, {
        "id": "300",
        "copyId": "06",
        "title": "Refactoring: Improving the Design of Existing Code",
        "publisher": "Addison-Wesley Professional",
        "authors": ["Martin Fowler"],
        "edition": "1ª",
        "year": "1999"
    }, {
        "id": "300",
        "copyId": "07",
        "title": "Refactoring: Improving the Design of Existing Code",
        "publisher": "Addison-Wesley Professional",
        "authors": ["Martin Fowler"],
        "edition": "1ª",
        "year": "1999"
    }, {
        "id": "301",
        "copyId": "92",
        "title": "Software Metrics: A Rigorous and Practical Approach",
        "publisher": "CRC Press",
        "authors": ["Norman Fenton", "James Bieman"],
        "edition": "3ª",
        "year": "2014"
    }, {
        "id": "400",
        "copyId": "08",
        "title": "Design Patterns: Elements of Reusable Object-Oriented Software",
        "publisher": "Addison-Wesley Professional",
        "authors": ["Erich Gamma", "Richard Helm", "Ralph Johnson", "John Vlissides"],
        "edition": "1ª",
        "year": "1994"
    }, {
        "id": "400",
        "copyId": "09",
        "title": "Design Patterns: Elements of Reusable Object-Oriented Software",
        "publisher": "Addison-Wesley Professional",
        "authors": ["Erich Gamma", "Richard Helm", "Ralph Johnson", "John Vlissides"],
        "edition": "1ª",
        "year": "1994"
    }, {
        "id": "401",
        "copyId": "76",
        "title": "UML Distilled: A Brief Guide to the Standard Object Modeling Language",
        "publisher": "Addison-Wesley Professional",
        "authors": ["Martin Fowler"],
        "edition": "3ª",
        "year": "2003"
    }]

def getUsers():
    return [Professor("100", "Carlos Lucena"),
            UndegraduateStudent("123", "João da Silva"),
            UndegraduateStudent("789", "Pedro Paulo"),
            PostgraduateStudent("456", "Luiz Fernando Rodrigues")]