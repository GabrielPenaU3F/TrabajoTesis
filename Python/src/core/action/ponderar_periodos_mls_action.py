import math

import numpy

from core.provider.service_provider import ServiceProvider


class PonderarPeriodosMLSAction:

    def __init__(self):
        self.operaciones_sobre_arrays_service = ServiceProvider.provide_operaciones_sobre_arrays_service()

    def execute(self, senal_mls, n_bits):

        periodos = self.separar_periodos(senal_mls, n_bits)
        sumatoria_periodos = list(numpy.zeros(int(math.pow(2, n_bits) - 1)))
        for i in range(len(periodos)):
            for j in range(len(sumatoria_periodos)):
                sumatoria_periodos[j] += periodos[i][j]
        return [x / len(periodos) for x in sumatoria_periodos]

    def separar_periodos(self, senal_mls, n_bits):
        periodos = []
        valores_crudos = senal_mls.get_valores().copy()
        longitud_periodo = int(math.pow(2, n_bits) - 1)
        cantidad_entera_de_periodos = int(senal_mls.get_longitud() / longitud_periodo)
        valores_mls = self.validar_longitud_de_senal(valores_crudos, cantidad_entera_de_periodos, longitud_periodo)

        for i in range(cantidad_entera_de_periodos):
            periodo_actual = []
            for j in range(longitud_periodo):
                periodo_actual.append(valores_mls[j])

            periodos.append(periodo_actual)
            valores_mls = valores_mls[longitud_periodo:len(valores_mls)]

        return periodos

    def validar_longitud_de_senal(self, valores_crudos, cantidad_entera_de_periodos, longitud_periodo):

        if cantidad_entera_de_periodos * longitud_periodo < len(valores_crudos):

            longitud_esperada_de_senal = (cantidad_entera_de_periodos + 1) * longitud_periodo
            valores_mls = self.operaciones_sobre_arrays_service.rellenar_con_ceros(valores_crudos,
                                                                                   longitud_esperada_de_senal)

        else:
            valores_mls = valores_crudos

        return valores_mls

