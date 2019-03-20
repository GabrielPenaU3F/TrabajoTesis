from threading import *
from src.core.domain.medicion import Medicion
from src.core.provider.action_provider import ActionProvider
from src.core.provider.queue_provider import QueueProvider
from src.core.provider.repository_provider import RepositoryProvider
from src.exception.excepciones import LundebyException
from src.core.domain.mensaje import Mensaje


class MedidorAcustico:

    def __init__(self):
        self.main_queue = QueueProvider.provide_main_queue()
        self.vista_detallada_queue = QueueProvider.provide_vista_detallada_queue()
        self.medir_respuesta_impulsional_action = ActionProvider.provide_medir_respuesta_impulsional_action()
        self.obtener_curva_decaimiento_action = ActionProvider.provide_obtener_curva_de_decaimiento_action()
        self.calcular_rt_action = ActionProvider.provide_calcular_rt_action()
        self.bandas_estandar_repository = RepositoryProvider.provide_bandas_estandar_repository()
        self.aplicar_filtro_octava_action = ActionProvider.provide_aplicar_filtro_octava_action()
        self.aplicar_filtro_tercio_octava_action = ActionProvider.provide_aplicar_filtro_tercio_de_octava_action()
        self.aplicar_ponderacion_A_action = ActionProvider.provide_aplicar_filtro_A_action()
        self.calcular_curvatura_action = ActionProvider.provide_calcular_curvatura_action()

    def medir(self, metodo):

        self.thread_medicion = Thread(target=self.efectuar_medicion, args=(metodo,), daemon=True)
        self.thread_medicion.start()

    def efectuar_medicion(self, metodo):

        fs = 48000
        respuesta_impulsional = self.medir_respuesta_impulsional_action.execute(metodo, fs)
        try:
            medicion = self.obtener_medicion_completa(respuesta_impulsional, fs)
            mensaje = Mensaje(destinatario="VistaPrincipal", mensaje="MedicionCompleta", paquete=medicion)
            self.main_queue.put(mensaje)
            return None
        except LundebyException:
            mensaje = Mensaje(destinatario="VistaPrincipal", mensaje="LundebyException")
            self.main_queue.put(mensaje)
            return None

    def efectuar_calculo(self, respuesta_impulsional, fs):
        try:
            medicion = self.obtener_medicion_completa(respuesta_impulsional, fs)
            mensaje = Mensaje(destinatario="VistaDetallada", mensaje="CalculoCompleto", paquete=medicion)
            self.vista_detallada_queue.put(mensaje)
            return None
        except LundebyException:
            mensaje = Mensaje(destinatario="VistaDetallada", mensaje="LundebyException")
            self.vista_detallada_queue.put(mensaje)
            return None

    def obtener_medicion_completa(self, respuesta_impulsional, fs):
        curva_decaimiento = self.obtener_curva_decaimiento_action.execute(respuesta_impulsional, fs)
        edt = self.calcular_rt_action.execute(curva_decaimiento, rt='EDT')
        t20 = self.calcular_rt_action.execute(curva_decaimiento, rt='T20')
        t30 = self.calcular_rt_action.execute(curva_decaimiento, rt='T30')
        curvatura = self.calcular_curvatura_action.execute(t20.get_rt(), t30.get_rt())
        return Medicion(respuesta_impulsional, curva_decaimiento, edt, t20, t30, curvatura, nivel=True)

    def calcular_parametros_acusticos(self, respuesta_impulsional, fs):
        self.thread_calculo = Thread(target=self.efectuar_calculo, args=(respuesta_impulsional, fs), daemon=True)
        self.thread_calculo.start()

    def obtener_medicion_en_octava(self, medicion, f_central, ponderacion_A):
        ri = medicion.get_respuesta_impulsional()
        if ponderacion_A:
            ri = self.aplicar_ponderacion_A_action.execute(ri)
        respuesta_impulsional_filtrada = self.aplicar_filtro_octava_action.execute(
            ri, f_central)
        self.calcular_parametros_acusticos(respuesta_impulsional_filtrada, respuesta_impulsional_filtrada.get_fs())

    def obtener_medicion_en_tercio_octava(self, medicion, f_central, ponderacion_A):
        ri = medicion.get_respuesta_impulsional()
        if ponderacion_A:
            ri = self.aplicar_ponderacion_A_action.execute(ri)
        respuesta_impulsional_filtrada = self.aplicar_filtro_tercio_octava_action.execute(
            ri, f_central)
        self.calcular_parametros_acusticos(respuesta_impulsional_filtrada, respuesta_impulsional_filtrada.get_fs())
