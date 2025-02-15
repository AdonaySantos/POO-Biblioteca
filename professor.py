from usuario import Usuario

class Professor(Usuario):
    def __init__(self, name, id):
        super().__init__(name, "Professor", id)

    