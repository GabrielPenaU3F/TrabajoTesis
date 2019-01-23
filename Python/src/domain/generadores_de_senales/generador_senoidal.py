import math


class GeneradorSenoidal():

    def generar_valores_senal_senoidal(self, longitud, fs):
        dominio_temporal = []
        for t in range(longitud):
            dominio_temporal.append(t / fs)
        valores = []
        for t in dominio_temporal:
            valores.append(math.sin(t))
        return valores
