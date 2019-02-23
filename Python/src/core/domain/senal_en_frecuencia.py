import numpy


class SenalEnFrecuencia:

    def __init__(self, dominio_frecuencial, valores):
        self.senal_en_frecuencia = {}
        for f in range(len(dominio_frecuencial)):
            self.senal_en_frecuencia[dominio_frecuencial[f]] = valores[f]

    def get_contenido(self):
        return self.senal_en_frecuencia

    def get(self, t):
        return self.senal_en_frecuencia.get(t)

    def get_dominio_frecuencial(self):
        return list(self.senal_en_frecuencia.keys())

    def get_modulo_valores(self):
        modulos = []
        for complejo in self.senal_en_frecuencia.values():
            modulos.append(numpy.abs(complejo))
        return modulos

    def get_fase_valores(self):
        fases = []
        for complejo in self.senal_en_frecuencia.values():
            fases.append(numpy.angle(complejo))
        return fases

    def get_valores_reales(self):
        reales = []
        for complejo in self.senal_en_frecuencia.values():
            reales.append(numpy.real(complejo))
        return reales

    def get_valores_imaginarios(self):
        imaginarios = []
        for complejo in self.senal_en_frecuencia.values():
            imaginarios.append(numpy.imag(complejo))
        return imaginarios

    def contiene(self, f):
        return self.senal_en_frecuencia.__contains__(f)

