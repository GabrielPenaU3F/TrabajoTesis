class Mensaje:

    def __init__(self, *args):

        self.mensaje = args[0]
        if len(args) == 2:
            self.contenido = args[1]

    def get_mensaje(self):
        return self.mensaje

    def get_contenido(self):
        if self.contenido:
            return self.contenido
