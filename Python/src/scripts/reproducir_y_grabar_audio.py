import numpy
from src.domain.lectograbador_de_audio import LectograbadorDeAudio
from src.domain.senal_audio import SenalAudio

datos = list(10*numpy.random.normal(0, 1, 441000))
fs = 44100
audio = LectograbadorDeAudio().reproducir_y_grabar_audio(SenalAudio(fs, datos))
print("La wea")
