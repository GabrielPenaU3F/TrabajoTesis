import cmath


class PuntoSenalFrecuencia:

    def __init__(self, f, complejo):
        self.f = f
        self.complejo = complejo

    def get_f(self):
        return self.f

    def get_complejo(self):
        return self.complejo

    def get_modulo(self):
        return abs(self.complejo)

    def get_fase(self):
        return cmath.phase(self.complejo)
