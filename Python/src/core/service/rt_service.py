import math

from core.domain.tiempo_reverberacion import TiempoReverberacion


class RTService:

    def __init__(self):
        self.tiempos_reverberacion = {
            "EDT": self.calcular_edt,
            "T20": self.calcular_t20,
            "T30": self.calcular_t30,
        }
        from core.provider.service_provider import ServiceProvider
        self.recortar_service = ServiceProvider.provide_recortar_senales_service()
        self.estadistica_service = ServiceProvider.provide_estadistica_service()

    def calcular_rt(self, curva_decaimiento, rt):
        return self.tiempos_reverberacion.get(rt)(curva_decaimiento)

    def calcular_edt(self, curva_decaimiento):
        segmento = self.recortar_service.recortar_intervalo_en_amplitud_hasta_violar_condicion(curva_decaimiento, -10, 0)
        return self.calcular_parametros(segmento)

    def calcular_t20(self, curva_decaimiento):
        segmento = self.recortar_service.recortar_intervalo_en_amplitud_hasta_violar_condicion(curva_decaimiento, -25, -5)
        return self.calcular_parametros(segmento)

    def calcular_t30(self, curva_decaimiento):
        segmento = self.recortar_service.recortar_intervalo_en_amplitud_hasta_violar_condicion(curva_decaimiento, -35, -5)
        return self.calcular_parametros(segmento)

    def calcular_parametros(self, segmento):
        recta_regresion = self.estadistica_service.efectuar_regresion_lineal(
            segmento.get_dominio_temporal(), segmento.get_valores())
        rt = recta_regresion.get_preimagen(-60)
        coef_correlacion = self.estadistica_service.calcular_coeficiente_de_correlacion(
            segmento, recta_regresion, tipo='iso')
        xi = 1000 * (1 - math.pow(coef_correlacion, 2))
        return TiempoReverberacion(rt, coef_correlacion, xi)



