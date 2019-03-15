from matplotlib import pyplot

from src.core.domain.generadores_de_senales.generador_senoidal import GeneradorSenoidal

senoide = GeneradorSenoidal().generar_senoide(48000, 3, 1, 1, 0)
pyplot.plot(senoide.get_dominio_temporal(), senoide.get_valores())
pyplot.show()