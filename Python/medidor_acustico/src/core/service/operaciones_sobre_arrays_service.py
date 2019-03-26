import numpy


class OperacionesSobreArraysService:

    def obtener_longitud_del_array_mas_corto(self, array_uno, array_dos):
        if len(array_uno) >= len(array_dos): return len(array_dos)
        else: return len(array_uno)

    def rellenar_con_ceros(self, senal, longitud_final):
        cantidad_de_ceros = longitud_final - len(senal)
        senal += list(numpy.zeros(cantidad_de_ceros))
        return senal
