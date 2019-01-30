import math


class SenalEnTiempo:

    def __init__(self, dominio_temporal, valores):
        self.senal_en_tiempo = {}
        for t in range(len(dominio_temporal)):
            self.senal_en_tiempo[dominio_temporal[t]] = valores[t]

        self.energia_total = self.calcular_energia()

    def get_contenido(self):
        return self.senal_en_tiempo

    def get(self, t):
        return self.senal_en_tiempo.get(t)

    def get_dominio_temporal(self):
        return list(self.senal_en_tiempo.keys())

    def get_valores(self):
        return list(self.senal_en_tiempo.values())

    def contiene(self, t):
        return self.senal_en_tiempo.__contains__(t)

    def get_energia_total(self):
        return self.energia_total

    def calcular_energia(self):
        energia = 0
        Ts = self.get_dominio_temporal()[1] - self.get_dominio_temporal()[0]
        for valor in self.get_valores():
            energia += math.pow(valor, 2) * Ts
        return energia
