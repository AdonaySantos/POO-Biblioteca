# A classe usuário será uma classe abstrata para as classes aluno, e professor
# Vai conter os métodos que queremos que os alunos e professores tenham em comum!

class Usuario:
    def __init__(self, name, kind, id):
        self.name = name
        self.kind = kind
        self.__id = id
        self.__borrowed_books = {}
        
    def get_user(self):
        return "Usuário: " + self.name + " Tipo: " + self.kind + " ID: " + self.__id
    
    def get_borrowed_books(self):
        return self.__borrowed_books.values()
        
    def take_book(self, book):
        if self.__borrowed_books[book.isbn]:
            raise ValueError(f"{self.name} has already taken this book")
        
        self.__borrowed_books[book.isbn] = book
        return "The user - Name: " + self.name + " Id: " + self.__id + " - borrowed the book" + book.title
        
    def returning_book(self, book):
        if not self.__borrowed_books[book.isbn]:
            raise ValueError(f"{self.name} hasn't already taken this book")
        
        self.__borrowed_books.pop[book.isbn]
        return "The user - Name: " + self.name + " Id: " + self.__id + " - returned the book" + book.title