from usuario import Usuario

class Aluno(Usuario):
    def __init__(self, name, id):
        super().__init__(name, "Aluno", id)