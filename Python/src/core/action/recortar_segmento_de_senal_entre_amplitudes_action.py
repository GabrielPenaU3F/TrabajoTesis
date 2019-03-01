from src.core.domain.senal_audio import SenalAudio


class RecortarSegmentoDeSenalEntreAmplitudesAction:

    def execute(self, senal, a_inf, a_sup):
        valores = senal.get_valores()
        dominio_temporal = senal.get_dominio_temporal()
        nuevo_dominio = []
        nuevos_valores = []
        ha_entrado_al_rango = False
        for k in range(len(dominio_temporal)):
            if self.pertenece_al_rango_especificado(valores[k], a_inf, a_sup):
                ha_entrado_al_rango = True
                nuevo_dominio.append(dominio_temporal[k])
                nuevos_valores.append(valores[k])
            elif ha_entrado_al_rango is True and not self.pertenece_al_rango_especificado(valores[k], a_inf, a_sup):
                break

        return SenalAudio(senal.get_fs(), nuevo_dominio, nuevos_valores)

    def pertenece_al_rango_especificado(self, valor, a_inf, a_sup):
        return a_inf <= valor <= a_sup
