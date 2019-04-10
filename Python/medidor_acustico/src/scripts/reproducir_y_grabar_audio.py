import numpy

from src.core.domain.generadores_de_senales.generador_mls import GeneradorMLS
from src.core.domain.equipo_de_audio import EquipoDeAudio

fs = 44100
datos = list(10*numpy.random.normal(0, 1, 441000))
senal_mls = GeneradorMLS().generar_senal_mls(17, 8, fs)
audio = EquipoDeAudio().reproducir_y_grabar_audio(senal_mls)
print('La wea')
