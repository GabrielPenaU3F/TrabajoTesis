from src.core.domain.senal_audio import SenalAudio


class RecortarSenalesService:

    def recortar_intervalo_en_amplitud_hasta_violar_condicion(self, senal, a_inf, a_sup):
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

    def recortar_en_tiempo(self, senal, t_inicio, t_fin):
        dominio_temporal = senal.get_dominio_temporal()
        valores = senal.get_valores()
        nuevo_dominio = []
        nuevos_valores = []
        for i in range(len(dominio_temporal)):
            if t_inicio <= dominio_temporal[i] <= t_fin:
                nuevo_dominio.append(dominio_temporal[i])
                nuevos_valores.append(valores[i])

        return SenalAudio(senal.get_fs(), nuevo_dominio, nuevos_valores)
