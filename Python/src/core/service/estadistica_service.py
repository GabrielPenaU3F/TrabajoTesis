import math

import numpy

from core.domain.recta import Recta
from exception.excepciones import RegresionException


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

    def calcular_coeficiente_de_correlacion(self, arg1, arg2, tipo):

        if tipo == 'iso':
        # Coeficiente de correlación valores - recta estimada según ISO 3382-2
            segmento_real = arg1
            recta_estimada = arg2
            valores_reales = segmento_real.get_valores()
            valores_estimados = recta_estimada.calcular_valores(segmento_real.get_dominio_temporal())
            media_valores_reales = numpy.mean(valores_reales)

            numerador = 0
            denominador = 0
            for i in range(segmento_real.get_longitud()):
                numerador = numerador + math.pow(valores_estimados[i] - media_valores_reales, 2)
                denominador = denominador + math.pow(valores_reales[i] - media_valores_reales, 2)

            return math.sqrt(numerador / denominador)

        elif tipo == 'pearson':
        # Coeficiente de Pearson entre dos variables
            x = arg1
            y = arg2
            n = len(x)

            x_media = numpy.mean(x)
            y_media = numpy.mean(y)

            numerador = 0
            suma_desv_cuadradas_x = 0
            suma_desv_cuadradas_y = 0
            for i in range(n):
                numerador = numerador + (x[i] - x_media) * (y[i] - y_media)
                suma_desv_cuadradas_x = suma_desv_cuadradas_x + (math.pow((x[i] - x_media), 2))
                suma_desv_cuadradas_y = suma_desv_cuadradas_y + (math.pow((y[i] - y_media), 2))

            denominador = math.sqrt(suma_desv_cuadradas_x) * math.sqrt(suma_desv_cuadradas_y)

            return numerador / denominador


