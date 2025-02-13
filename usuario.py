# A classe usuário será uma classe abstrata para as classes aluno, e professor
# Vai conter os métodos que queremos que os alunos e professores tenham em comum!

class Usuário:
    def __init__(self, name, kind, id):
        self.name = name
        self.kind = kind
        self.id = id
        self.borrowed_books = []
        
    def take_book(self, book):
        if self.borrowed_books[book]:
            raise ValueError(f"{self.name} has already taken this book")
        
        self.borrowed_book.append(book)
        
        
    def return_book(self, book):
        if not self.borrowed_book[book]:
            raise ValueError(f"{self.name} hasn't already taken this book")
        
        self.borrowed_book.remove[book]