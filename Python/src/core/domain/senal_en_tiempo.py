from src.exception.excepciones import IndiceSenalException


class SenalEnTiempo:

    def __init__(self, dominio_temporal, valores):
        self.senal_en_tiempo = {}
        for t in range(len(dominio_temporal)):
            self.senal_en_tiempo[dominio_temporal[t]] = valores[t]

        from src.core.provider.action_provider import ActionProvider
        self.energia_total = ActionProvider.provide_calcular_energia_total_action().execute(self)
        self.senal_en_db = None

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

    def get_indice_en_t(self, t):

        dominio_temporal = self.get_dominio_temporal()
        if t < dominio_temporal[0] or t > dominio_temporal[len(dominio_temporal) - 1]:
            raise IndiceSenalException("El instante de tiempo solicitado no pertenece al dominio de la señal")

        for i in range(len(dominio_temporal) - 1):
            if dominio_temporal[i] == t or (dominio_temporal[i] < t < dominio_temporal[i + 1]):
                return i
        return len(dominio_temporal)

    def get_senal_en_db(self):
        if self.senal_en_db is None:
            from src.core.provider.action_provider import ActionProvider
            self.senal_en_db = ActionProvider.provide_transformar_a_escala_logaritmica_normalizada_action().execute(
                self)
        return self.senal_en_db

