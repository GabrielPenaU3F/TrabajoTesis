from src.controller.pantalla_con_graficas_controller import PantallaConGraficasController
from src.core.domain.medidor_acustico import MedidorAcustico
from src.core.provider.action_provider import ActionProvider
from src.core.provider.repository_provider import RepositoryProvider
from src.core.provider.subject_provider import SubjectProvider
from src.core.domain.mensaje import Mensaje


class VistaDetalladaController(PantallaConGraficasController):


    def __init__(self, view):
        super().__init__(view)
        self.master = "VistaDetallada"
        self.string_repository = RepositoryProvider.provide_string_repository()
        self.vista_detallada_subject = SubjectProvider.provide_vista_detallada_subject()
        self.pantalla_instrucciones_vista_detallada_subject = SubjectProvider.\
            provide_pantalla_instrucciones_vista_detallada_subject()
        self.pantalla_instrucciones_vista_detallada_subject.subscribe(on_next=lambda mensaje: self.procesar(mensaje))
        self.medicion_repository = RepositoryProvider.provide_medicion_repository()
        self.medidor_acustico = MedidorAcustico()
        self.transformar_a_db_action = ActionProvider.provide_transformar_a_escala_logaritmica_normalizada_action()
        self.calculos_por_tipo_de_banda = {
            'OCTAVA': self.medidor_acustico.obtener_medicion_en_octava,
            'TERCIO_OCTAVA': self.medidor_acustico.obtener_medicion_en_tercio_octava
        }

    def on_cerrar_ventana(self):
        mensaje_activar_boton = Mensaje(destinatario="VistaPrincipal", mensaje="ActivarBotonVistaDetallada")
        self.vista_detallada_subject.on_next(mensaje_activar_boton)
        self.view.ocultar_vista()

    def on_calcular(self):
        self.activar_progressbar()
        self.bloquear_controles()
        ponderacion_A_activa = self.view.verificar_ponderacion_A()
        tab_activa = self.view.get_tab_activa()
        medicion = self.medicion_repository.get_medicion()
        f_central = tab_activa.get_frecuencia_central_banda_seleccionada()
        self.calculos_por_tipo_de_banda.get(tab_activa.get_tipo())(
            medicion, f_central, ponderacion_A=ponderacion_A_activa)

    def on_mostrar_instrucciones(self):
        self.desactivar_boton_instrucciones()
        from src.core.domain.coordinador_de_vistas import CoordinadorDeVistas
        CoordinadorDeVistas.mostrar_vista("VistaDetalladaInstrucciones")

    def desactivar_boton_instrucciones(self):
        self.view.desactivar_boton_instrucciones()

    def activar_boton_instrucciones(self):
        self.view.activar_boton_instrucciones()

    def finalizar_calculo(self, paquete):
        self.unbindear_evento_root("Configure")
        self.mostrar_medicion_en_vista(paquete)
        self.desactivar_progressbar()
        self.desbloquear_controles()

    def mostrar_medicion_en_vista(self, medicion):
        nivel_respuesta_impulsional = medicion.get_nivel_respuesta_impulsional()
        self.view.graficar(nivel_respuesta_impulsional, medicion.get_curva_decaimiento())
        self.view.mostrar_tiempos_de_reverberacion(
            medicion.get_edt().get_rt(), medicion.get_t20().get_rt(), medicion.get_t30().get_rt())
        self.view.mostrar_parametros_de_linealidad(
            medicion.get_edt(), medicion.get_t20(), medicion.get_t30(), medicion.get_curvatura())

    def mostrar_error_lundeby(self):
        self.view.mostrar_error_lundeby(self.string_repository.get_mensaje_error_lundeby())
        self.desbloquear_controles()
        self.desactivar_progressbar()

    def get_medicion(self):
        return self.medicion_repository.get_medicion()

    def activar_progressbar(self):
        self.view.activar_progressbar()

    def desactivar_progressbar(self):
        self.view.desactivar_progressbar()
