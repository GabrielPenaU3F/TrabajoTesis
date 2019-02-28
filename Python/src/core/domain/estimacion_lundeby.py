class EstimacionLundeby:

    def __init__(self, limite, termino_correccion):
        self.limite = limite
        self.termino_correccion = termino_correccion

    def get_limite(self):
        return self.limite

    def get_termino_correccion(self):
        return self.termino_correccion
