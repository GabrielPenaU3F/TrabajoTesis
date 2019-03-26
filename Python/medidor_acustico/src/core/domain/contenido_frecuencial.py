import cmath


class ContenidoFrecuencial:

    def __init__(self, puntos_frecuenciales):
        self.puntos_frecuenciales = puntos_frecuenciales
        self.dominio_frecuencial = []
        self.valores_complejos = []
        for i in range(len(puntos_frecuenciales)):
            self.dominio_frecuencial.append(puntos_frecuenciales[i].get_f())
            self.valores_complejos.append(puntos_frecuenciales[i].get_complejo())

    def get_dominio_frecuencial(self):
        return self.dominio_frecuencial

    def get_valores_complejos(self):
        return self.valores_complejos

    def get_modulos(self):
        return [abs(z) for z in self.valores_complejos]

    def get_fases(self):
        return [cmath.phase(z) for z in self.valores_complejos]

    def get_muestra(self, muestra_correspondiente):
        return self.valores_complejos[muestra_correspondiente]
