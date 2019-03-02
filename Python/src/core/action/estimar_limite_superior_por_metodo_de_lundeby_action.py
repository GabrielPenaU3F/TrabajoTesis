import math
import numpy
from src.core.domain.senal_audio import SenalAudio
from src.core.provider.service_provider import ServiceProvider
from src.exception.excepciones import LundebyException


class EstimarLimiteSuperiorPorMetodoDeLundebyAction:

    def __init__(self):
        from src.core.provider.action_provider import ActionProvider
        self.estadistica_service = ServiceProvider.provice_estadistica_service()
        self.aplicar_filtro_media_movil_action = ActionProvider.provide_aplicar_filtro_media_movil_action()
        self.transformar_a_escala_logaritmica_normalizada_action = ActionProvider.\
            provide_transformar_a_escala_logaritmica_normalizada_action()
        self.recortar_en_tiempo_action = ActionProvider.provide_recortar_segmento_de_senal_en_tiempo_action()
        self.recortar_en_amplitud_action = ActionProvider.provide_recortar_segmento_de_senal_entre_amplitudes_action()
        self.calcular_energia_total_action = ActionProvider.provide_calcular_energia_total_action()

    def execute(self, respuesta_impulsional):

        fs = respuesta_impulsional.get_fs()
        h = respuesta_impulsional.get_valores()
        t = respuesta_impulsional.get_dominio_temporal()
        duracion = respuesta_impulsional.get_duracion()
        h_cuadrado = numpy.power(h, 2)

        # Paso 1: se pasa un filtro de media móvil y se pasa h a escala logarítmica
        longitud_filtro = round(0.030 * fs)  # 30ms, parametro ajustable
        h_cuadrado_suave = self.aplicar_filtro_media_movil_action.execute(
            SenalAudio(fs, t, h_cuadrado), longitud_filtro)
        h_cuadrado_db = self.transformar_a_escala_logaritmica_normalizada_action.execute(h_cuadrado_suave)
        senal_h_cuadrado_db = SenalAudio(fs, t, h_cuadrado_db.get_valores())

        # Paso 2: se estima el nivel de ruido de fondo
        porcentaje_de_senal_que_es_cola = 10  # 10%, parametro ajustable
        tiempo_cola = round(senal_h_cuadrado_db.get_duracion() * porcentaje_de_senal_que_es_cola / 100)
        cola = self.recortar_en_tiempo_action.execute(senal_h_cuadrado_db, duracion - tiempo_cola, duracion)
        nivel_de_ruido_de_fondo = numpy.mean(cola.get_valores())

        # Paso 3: buscar la recta de regresión de la región con ordenada 0 por encima del ruido de fondo
        nivel_inferior_estimacion = nivel_de_ruido_de_fondo + 10  # Parámetro ajustable
        curva_decaimiento = self.recortar_en_amplitud_action.execute(
            senal_h_cuadrado_db, nivel_inferior_estimacion, 0)
        recta_regresion = self.estadistica_service.efectuar_regresion_lineal(
            curva_decaimiento.get_dominio_temporal(), curva_decaimiento.get_valores(), True)

        # Paso 4: determinar el punto de cruce entre la recta y el ruido de fondo
        t_cruce = nivel_de_ruido_de_fondo / recta_regresion.get_pendiente()

        # Paso 5: determinar una nueva ventana para el filtro de media móvil, dividiendo la región de decaimiento
        # en varios intervalos
        valor_en_el_cruce = senal_h_cuadrado_db.get_valor_en(t_cruce)
        cantidad_de_intervalos_cada_10_db_de_decaimiento = 5  # Parametro ajustable
        cantidad_intervalos = math.floor(abs(valor_en_el_cruce) * cantidad_de_intervalos_cada_10_db_de_decaimiento / 10)
        longitud_filtro = math.floor(t_cruce * fs / cantidad_intervalos)

        # Paso 6: aplicar el nuevo filtro
        senal_h_cuadrado_db_filtrada = self.aplicar_filtro_media_movil_action.execute(
            senal_h_cuadrado_db, longitud_filtro)

        # Los siguientes pasos constituirán una iteración. El algoritmo requiere un total de 5 iteraciones

        recta_decaimiento = None
        for i in range(5):

            # Paso 7: Determinar el nivel de ruido de fondo de la nueva señal, a partir del nuevo punto de cruce estimado
            valor_en_el_cruce = senal_h_cuadrado_db_filtrada.get_valor_en(t_cruce)
            porcentaje_minimo_ri = 10  # Porcentaje minimo que debe quedar de la señal luego del truncado
            margen_de_db = 5  # Parámetro ajustable
            minimo_t_posible = duracion * porcentaje_minimo_ri / 100

            if self.se_eliminaria_mas_del_90_porciento_de_ri(
                    senal_h_cuadrado_db_filtrada.get_valor_en(minimo_t_posible), valor_en_el_cruce, margen_de_db):

                senal_nivel_ruido_de_fondo = self.recortar_en_tiempo_action.execute(
                    senal_h_cuadrado_db_filtrada, minimo_t_posible, senal_h_cuadrado_db_filtrada.get_duracion())

            else:
                t_cruce_preliminar = self.encontrar_punto_de_cruce_preliminar(
                    senal_h_cuadrado_db_filtrada, valor_en_el_cruce, margen_de_db)
                senal_nivel_ruido_de_fondo = self.recortar_en_tiempo_action.execute(
                    senal_h_cuadrado_db_filtrada, t_cruce_preliminar, senal_h_cuadrado_db_filtrada.get_duracion())

            nivel_de_ruido_de_fondo = numpy.mean(senal_nivel_ruido_de_fondo.get_valores())

            # Paso 8: Obtener la recta de regresión del decaimiento tardío
            distancia_inicio_decaimiento_tardio_al_ruido_de_fondo = 20  # Parámetro ajustable
            distancia_final_decaimiento_tardio_al_ruido_de_fondo = 7  # Parámetro ajustable
            curva_decaimiento_tardio = self.recortar_en_amplitud_action.execute(
                senal_h_cuadrado_db_filtrada,
                nivel_de_ruido_de_fondo + distancia_final_decaimiento_tardio_al_ruido_de_fondo,
                nivel_de_ruido_de_fondo + distancia_inicio_decaimiento_tardio_al_ruido_de_fondo)
            recta_decaimiento = self.estadistica_service.efectuar_regresion_lineal(
                curva_decaimiento_tardio.get_dominio_temporal(), curva_decaimiento_tardio.get_valores())

            # Paso 9:
            t_cruce = (nivel_de_ruido_de_fondo - recta_decaimiento.get_ordenada()) / recta_decaimiento.get_pendiente()

        if t_cruce > duracion: raise LundebyException("El tiempo de truncado es mayor a la duración de la señal")

        return t_cruce

    def se_eliminaria_mas_del_90_porciento_de_ri(self, valor_minimo, valor_en_el_cruce, margen_de_db):
        return valor_minimo < valor_en_el_cruce + margen_de_db

    def encontrar_punto_de_cruce_preliminar(self, senal, valor_en_el_cruce, margen_de_db):
        dominio_temporal = senal.get_dominio_temporal()
        valores = senal.get_valores()
        for i in range(len(valores)):
            if valores[i] <= valor_en_el_cruce + margen_de_db:
                return dominio_temporal[i]
        raise LundebyException("Error en la estimación")
