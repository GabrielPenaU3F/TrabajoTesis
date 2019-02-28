class ContenidoTemporal:

    def __init__(self, puntos_temporales):
        self.puntos_temporales = puntos_temporales
        self.dominio_temporal = []
        self.valores = []
        for i in range(len(puntos_temporales)):
            self.dominio_temporal.append(puntos_temporales[i].get_t())
            self.valores.append(puntos_temporales[i].get_amplitud())

    def get_dominio_temporal(self):
        return self.dominio_temporal

    def get_valores(self):
        return self.valores

    def get_valor_en(self, t):
        for i in range(len(self.puntos_temporales) - 1):

            if self.puntos_temporales[i].get_t() == t:
                return self.puntos_temporales[i].get_amplitud()

            elif self.puntos_temporales[i+1].get_t() > t > self.puntos_temporales[i].get_t():
                return self.puntos_temporales[i].get_amplitud()
