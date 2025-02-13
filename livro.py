# A classe livro será um criador de objetos, que vai servir para gerar e atualizar a disponibilidade dos livros da nossa biblioteca
# O objeto livro deve conter: Titulo, Gêneros, Id, Disponibilidade, Autor

class Livros:
    def __init__(self, title, genre, author, isbn):
        self.title = title
        self.genre = genre
        self.author = author
        self.id = isbn
        self.available = True
    
    def borrow(self):
        if not self.available:
            raise ValueError("This book is not available!")

        self.available = False
        return "The book " + self.title + " was successsfully borrowed"