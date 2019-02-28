from src.core.domain.senal_audio import SenalAudio

class RecortarSegmentoDeSenalEntreAmplitudesAction:

    def execute(self, senal, a_inf, a_sup):
        valores = senal.get_valores()
        dominio_temporal = senal.get_dominio_temporal()
        nuevo_dominio = []
        nuevos_valores = []
        for k in range(len(dominio_temporal)):
            if a_inf <= valores[k] <= a_sup:
                nuevo_dominio.append(dominio_temporal[k])
                nuevos_valores.append(valores[k])
        return SenalAudio(senal.get_fs(), nuevo_dominio, nuevos_valores)
