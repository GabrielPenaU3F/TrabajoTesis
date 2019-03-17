from src.core.domain.medicion import Medicion
from src.core.domain.medidor_acustico import MedidorAcustico
from src.core.provider.action_provider import ActionProvider
from src.core.provider.procesador_mensajes_provider import ProcesadorMensajesProvider
from src.core.provider.queue_provider import QueueProvider
from src.core.provider.repository_provider import RepositoryProvider
from src.core.provider.subject_provider import SubjectProvider
from src.messages.mensaje import Mensaje
from src.view.vista_detallada.instrucciones_vista_detallada_view import InstruccionesVistaDetalladaView


class VistaDetalladaController:

    def __init__(self, view):
        self.root_bindings = []
        self.binding_eventos_repository = RepositoryProvider.provide_binding_eventos_repository()
        self.string_repository = RepositoryProvider.provide_string_repository()
        self.view = view
        self.procesador_mensajes = ProcesadorMensajesProvider.provide_procesador_mensajes()
        self.vista_detallada_subject = SubjectProvider.provide_vista_detallada_subject()
        self.pantalla_instrucciones_vista_detallada_subject = SubjectProvider.\
            provide_pantalla_instrucciones_vista_detallada_subject()
        self.pantalla_instrucciones_vista_detallada_subject.subscribe(on_next=lambda mensaje: self.procesar(mensaje))
        self.medicion_repository = RepositoryProvider.provide_medicion_repository()
        self.vista_detallada_queue = QueueProvider.provide_vista_detallada_queue()
        self.medidor_acustico = MedidorAcustico()
        self.transformar_a_db_action = ActionProvider.provide_transformar_a_escala_logaritmica_normalizada_action()
        self.calculos_por_tipo_de_banda = {
            'OCTAVA': self.medidor_acustico.obtener_medicion_en_octava,
            'TERCIO_OCTAVA': self.medidor_acustico.obtener_medicion_en_tercio_octava
        }

    def actualizar(self):
        if not self.vista_detallada_queue.empty():
            mensaje = self.vista_detallada_queue.get()
            metodo_a_ejecutar = getattr(self, self.procesador_mensajes.get_mensaje(mensaje.get_mensaje()))
            metodo_a_ejecutar(mensaje)

    def on_cerrar_ventana(self):
        mensaje_activar_boton = Mensaje("ActivarBotonVistaDetallada")
        self.vista_detallada_subject.on_next(mensaje_activar_boton)
        self.view.ocultar_vista()

    def on_calcular(self):
        self.bloquear_controles()
        self.activar_progressbar()
        ponderacion_A = self.view.verificar_ponderacion_A()
        tab_activa = self.view.get_tab_activa()
        medicion = self.medicion_repository.get_medicion()
        f_central = tab_activa.get_frecuencia_central_banda_seleccionada()
        self.calculos_por_tipo_de_banda.get(tab_activa.get_tipo())(medicion, f_central, ponderacion_A=ponderacion_A)

    def on_mostrar_instrucciones(self):
        self.desactivar_boton_instrucciones()
        InstruccionesVistaDetalladaView()

    def desactivar_boton_instrucciones(self):
        self.view.desactivar_boton_instrucciones()

    def activar_boton_instrucciones(self):
        self.view.activar_boton_instrucciones()

    def procesar(self, mensaje):
        metodo_a_ejecutar = getattr(self, self.procesador_mensajes.get_mensaje(mensaje.get_mensaje()))
        metodo_a_ejecutar()

    def finalizar_calculo(self, mensaje):
        self.unbindear_evento_root("Configure")
        medicion = mensaje.get_contenido()
        self.mostrar_medicion_en_vista(medicion)
        self.vista_detallada_queue.task_done()
        self.desactivar_progressbar()
        self.desbloquear_controles()

    def bloquear_controles(self):
        self.view.bloquear_controles()

    def desbloquear_controles(self):
        self.view.desbloquear_controles()

    def mostrar_medicion_en_vista(self, medicion):
        respuesta_impulsional = medicion.get_respuesta_impulsional()
        nivel_respuesta_impulsional = self.transformar_a_db_action.execute(respuesta_impulsional)
        self.view.graficar(nivel_respuesta_impulsional, medicion.get_curva_decaimiento())
        self.view.mostrar_tiempos_de_reverberacion(
            medicion.get_edt().get_rt(), medicion.get_t20().get_rt(), medicion.get_t30().get_rt())
        self.view.mostrar_parametros_de_linealidad(
            medicion.get_edt(), medicion.get_t20(), medicion.get_t30(), medicion.get_curvatura())

    def mostrar_error_lundeby(self, mensaje):
        self.view.mostrar_error_lundeby(self.string_repository.get_mensaje_error_lundeby())
        self.vista_detallada_queue.task_done()
        self.desbloquear_controles()
        self.desactivar_progressbar()

    def get_medicion_nivel_db(self):
        medicion = self.medicion_repository.get_medicion()
        ri_db = self.transformar_a_db_action.execute(medicion.get_respuesta_impulsional())
        return Medicion(ri_db, medicion.get_curva_decaimiento(), medicion.get_edt(), medicion.get_t20(),
                        medicion.get_t30(), medicion.get_curvatura())

    def get_medicion(self):
        return self.medicion_repository.get_medicion()

    def activar_progressbar(self):
        self.view.activar_progressbar()

    def desactivar_progressbar(self):
        self.view.desactivar_progressbar()

    def bindear_eventos_root(self):
        eventos = self.binding_eventos_repository.get_eventos()
        for clave_evento in eventos:
            self.bindear_evento_root(clave_evento)

    def bindear_evento_root(self, clave_evento):
        binding = self.binding_eventos_repository.get_binding(clave_evento)
        if not self.root_bindings.__contains__(binding.get_evento()):
            self.root_bindings.append(binding.get_evento())
            self.view.bindear_evento_root(binding)

    def unbindear_evento_root(self, clave_evento):
        binding = self.binding_eventos_repository.get_binding(clave_evento)
        if self.root_bindings.__contains__(binding.get_evento()):
            self.root_bindings.remove(binding.get_evento())
            self.view.unbindear_evento_root(binding)
