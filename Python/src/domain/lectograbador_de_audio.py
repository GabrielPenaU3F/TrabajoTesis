import numpy
import sounddevice
from src.domain.senal_audio import SenalAudio


class LectograbadorDeAudio:

    def reproducir_y_grabar_audio(self, senal):
        audio = sounddevice.playrec(numpy.array(senal.get_valores()), samplerate=senal.get_fs(), channels=1,
                                    dtype='float64', blocking=True).tolist()
        audio = [x[0] for x in audio]
        return SenalAudio(senal.get_fs(), audio)
