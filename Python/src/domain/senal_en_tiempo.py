class SenalEnTiempo:

    def __init__(self, dominio_temporal, valores):
        self.senal_en_tiempo = {}
        for t in range(len(dominio_temporal)):
            self.senal_en_tiempo[dominio_temporal[t]] = valores[t]

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
