class Recta:

    def __init__(self, pendiente, ordenada):
        self.pendiente = pendiente
        self.ordenada = ordenada

    def get_pendiente(self):
        return self.pendiente

    def get_ordenada(self):
        return self.ordenada

    def get_imagen(self, x):
        return self.pendiente * x + self.ordenada

    def get_preimagen(self, y):
        return (y - self.ordenada)/self.pendiente
