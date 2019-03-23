from tkinter import Toplevel, Frame, Button, DISABLED, NORMAL, messagebox
from controller.vista_detallada_controller import VistaDetalladaController
from core.provider.repository_provider import RepositoryProvider
from view.view_con_graficas import ViewConGraficas
from view.vista_detallada.tab_control import TabControl
from view.vista_detallada.tab_octava import TabOctava
from view.vista_detallada.tab_tercio_octava import TabTercioOctava


class VistaDetalladaView(ViewConGraficas):

    def __init__(self):

        super().__init__(VistaDetalladaController(self), Toplevel())

        self.bandas_estandar_repository = RepositoryProvider.provide_bandas_estandar_repository()

        self.main_frame = self.construir_main_frame()

        self.construir_tabs()

        self.construir_botones()

        self.ocultar_vista()

        self.root.after(0, self.bindear_eventos_root)

        self.root.after(0, self.configurar_root())

        self.refrescar()

    def configurar_root(self):
        # ----- Configuracion del root ------
        self.root.title("Medidor Acústico - Vista detallada")
        super(VistaDetalladaView, self).configurar_root()

    def construir_main_frame(self):
        main_frame = Frame(self.root)
        main_frame.config(width="700", height="700")
        main_frame.pack(fill="both", expand="True", padx=20, pady=20)
        return main_frame

    def construir_tabs(self):

        self.tab_control = TabControl(self.main_frame)
        self.tab_octava = TabOctava(self, self.tab_control)
        self.tab_tercio_octava = TabTercioOctava(self, self.tab_control)

    def on_calcular(self):
        self.controller.on_calcular()

    def on_mostrar_instrucciones(self):
        self.controller.on_mostrar_instrucciones()

    def desactivar_boton_instrucciones(self):
        self.boton_instrucciones.config(command="")

    def activar_boton_instrucciones(self):
        self.boton_instrucciones.config(command=self.controller.on_mostrar_instrucciones)

    def graficar(self, nivel_respuesta_impulsional, curva_decaimiento):
        tab_activa = self.get_tab_activa()
        tab_activa.graficar(nivel_respuesta_impulsional, curva_decaimiento)

    def mostrar_tiempos_de_reverberacion(self, edt, t20, t30):
        tab_activa = self.get_tab_activa()
        tab_activa.mostrar_tiempos_de_reverberacion(edt, t20, t30)

    def mostrar_parametros_de_linealidad(self, edt, t20, t30, curvatura):
        tab_activa = self.get_tab_activa()
        tab_activa.mostrar_parametros_de_linealidad(edt, t20, t30, curvatura)

    def construir_botones(self):

        self.boton_instrucciones = Button(self.main_frame)
        self.boton_instrucciones.config(text="Instrucciones", command=self.controller.on_mostrar_instrucciones,
                                        bg="#5e0606")
        self.boton_instrucciones.grid(row=1, column=0, sticky="sw", pady=(20, 0))

        self.boton_salir = Button(self.main_frame)
        self.boton_salir.config(text="Salir", command=self.controller.on_cerrar_ventana, bg="#5e0606")
        self.boton_salir.grid(row=1, column=1, sticky="se", pady=(20, 0))

    def get_tab_activa(self):
        return self.tab_control.get_tab_activa()

    def bloquear_controles(self):
        self.boton_salir.config(state=DISABLED)
        self.tab_control.desactivar()

    def desbloquear_controles(self):
        self.boton_salir.config(state=NORMAL)
        self.tab_control.activar()

    def verificar_ponderacion_A(self):
        return self.tab_control.verificar_ponderacion_A()

    def mostrar_error_lundeby(self, mensaje):
        messagebox.showerror("Error", mensaje)

    def graficar_medicion_general(self):
        medicion_general = self.controller.get_medicion()
        self.tab_control.graficar(
            medicion_general.get_nivel_respuesta_impulsional(), medicion_general.get_curva_decaimiento())

    def mostrar_valores_generales(self):
        medicion_general = self.controller.get_medicion()
        self.tab_control.mostrar_tiempos_de_reverberacion(
            medicion_general.get_edt().get_rt(), medicion_general.get_t20().get_rt(), medicion_general.get_t30().get_rt())
        self.tab_control.mostrar_parametros_de_linealidad(
            medicion_general.get_edt(), medicion_general.get_t20(), medicion_general.get_t30(), medicion_general.get_curvatura())

    def activar_progressbar(self):
        tab_activa = self.get_tab_activa()
        tab_activa.activar_progressbar()

    def desactivar_progressbar(self):
        tab_activa = self.get_tab_activa()
        tab_activa.desactivar_progressbar()

    def ocultar_graficas(self):
        self.tab_control.ocultar_grafica()
        self.solicitud_de_redibujo = True

    def redibujar_canvas(self):
        self.tab_control.redibujar_canvas()
        self.solicitud_de_redibujo = False

    def mostrar_vista(self):
        super(VistaDetalladaView, self).mostrar_vista()
        self.mostrar_valores_generales()
        self.graficar_medicion_general()


