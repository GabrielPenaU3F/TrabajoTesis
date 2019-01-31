class OperacionesSobreArraysService:

    def obtener_longitud_del_array_mas_corto(self, array_uno, array_dos):
        if len(array_uno) >= len(array_dos): return len(array_dos)
        else: return len(array_uno)
