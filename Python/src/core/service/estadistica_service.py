import math

import numpy

from src.core.domain.recta import Recta
from src.exception.excepciones import RegresionException


class EstadisticaService:

    def efectuar_regresion_lineal(self, *args):

        x = args[0]
        y = args[1]

        if len(y) != len(x): raise RegresionException("Los datos de entrada son invalidos")

        if len(args) == 2 or args[2] == False:

            n = len(x)
            suma_xy = sum([x[i] * y[i] for i in range(n)])
            suma_x = sum(x)
            suma_y = sum(y)
            suma_x_cuadrado = sum([math.pow(x[i], 2) for i in range(n)])
            suma_x_al_cuadrado = math.pow(suma_x, 2)

            numerador = n * suma_xy - suma_x * suma_y
            denominador = n * suma_x_cuadrado - suma_x_al_cuadrado

            pendiente = numerador / denominador
            ordenada = numpy.mean(y) - pendiente * numpy.mean(x)
            return Recta(pendiente, ordenada)

        elif args[2]:

            n = len(x)
            suma_xy = sum([x[i] * y[i] for i in range(n)])
            suma_x = sum(x)

            pendiente = suma_xy / suma_x
            return Recta(pendiente, 0)


