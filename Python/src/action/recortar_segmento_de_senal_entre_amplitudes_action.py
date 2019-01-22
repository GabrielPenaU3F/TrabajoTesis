from src.domain.senal_en_tiempo import SenalEnTiempo


class RecortarSegmentoDeSenalEntreAmplitudesAction:

    def execute(self, senal_en_tiempo, a_inf, a_sup):
        nuevo_dominio = []
        nuevos_valores = []
        for k in senal_en_tiempo.get_dominio_temporal():
            if a_inf <= senal_en_tiempo.get(k) <= a_sup:
                nuevo_dominio.append(k)
                nuevos_valores.append(senal_en_tiempo.get(k))
        return SenalEnTiempo(nuevo_dominio, nuevos_valores)
