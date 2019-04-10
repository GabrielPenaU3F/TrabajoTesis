import numpy
import sounddevice
from src.core.domain.senal_audio import SenalAudio, DispositivoInaccesibleException


class EquipoDeAudio:

    def reproducir_y_grabar_audio(self, senal):
        try:
            audio = sounddevice.playrec(numpy.array(senal.get_valores()), samplerate=senal.get_fs(), channels=1,
                                        dtype='float64', blocking=True).tolist()
            audio = [x[0] for x in audio]
            return SenalAudio(senal.get_fs(), audio)

        except sounddevice.PortAudioError:
            raise DispositivoInaccesibleException("Dispositivo de salida o entrada de sonido inaccesible")
