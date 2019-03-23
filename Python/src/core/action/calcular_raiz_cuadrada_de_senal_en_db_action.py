from core.domain.senal_audio import SenalAudio


class CalcularRaizCuadradaDeSenalEnDbAction:

    def execute(self, senal):
        valores = senal.get_valores()
        return SenalAudio(senal.get_fs(), senal.get_dominio_temporal(), [valores[i]/2 for i in range(len(valores))])
