# a biblioteca vai ser como nosso banco de dados, vai listar todos os livros existentes, usuários (alunos e professores)
# imangino que utilizar uma estrutura de dicionários facilitará a organização de tudo
from livro import Livros

class Biblioteca:
    def __init__(self):
        self.books = {
            "978-6555665024" : Livros("As irmãs Blue", "FicçÃo Urbana", "Coco Mellors", "978-6555665024")
        }
        
    def add_book(self, book):
        self.books[book.isbn] = book
        
    def get_books(self):
        return "\n".join(f"book - {isbn} : {book}" for isbn, book in self.books.items())
    
    def search_books(self, filters):
        books = [
            (isbn, book) for isbn, book in self.books.items()
            if all(getattr(book, key, None) == value for key, value in filters.items())
        ]
        
        return books
    
    def borrow_book(self, book_title, user):
        available_books = self.search_books({"title" : book_title})
        
        if not available_books:
            print(f"No available books found for '{book_title}'.")
            return
        
        print("Available books:")
        for isbn, book in available_books:
            print(f"ISBN: {isbn} - {book.title}")
        
        ok = True
        while ok:
            try:
                isbn = input("Type the isbn of the chosen book or 0 to cancel")
                if isbn == "0":
                    print("Operation canceled.")
                    ok = False
                    continue
                
                book = self.books.get(isbn)
                if not book:
                    print("Invalid ISBN. Please try again")
                    continue
                
                user.take_book(book)
                print(book.borrow())
                ok = False
            except Exception as e:
                print(f"An error occurred: {e}")
                
    def return_book(self, isbn):
        return 