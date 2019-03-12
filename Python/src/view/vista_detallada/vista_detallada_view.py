from tkinter import Toplevel, Frame, ttk, Button, DISABLED, NORMAL, messagebox

from src.controller.vista_detallada_controller import VistaDetalladaController
from src.core.provider.repository_provider import RepositoryProvider
from src.view.vista_detallada.tab_control import TabControl
from src.view.vista_detallada.tab_octava import TabOctava
from src.view.vista_detallada.tab_tercio_octava import TabTercioOctava


class VistaDetalladaView:

    def __init__(self):

        self.controller = VistaDetalladaController(self)

        self.definir_estilos_ttk()

        self.bandas_estandar_repository = RepositoryProvider.provide_bandas_estandar_repository()

        self.root = self.construir_root()

        self.main_frame = self.construir_main_frame()

        self.construir_tabs()

        self.construir_botones()

        self.graficar_medicion_general()

        self.root.after(0, self.root.deiconify)  # Luego de construir toda la interface, permito mostrar la ventana

        self.refrescar()

        self.root.mainloop()

    def construir_root(self):
        root = Toplevel()
        root.withdraw()  # Inmediatamente después de la creación, oculto la ventana
        # ----- Configuracion del root ------
        root.title("Medidor Acústico - Vista detallada")
        root.iconbitmap("../resources/icons/mic_icon.ico")
        root.tk_setPalette(background='#831212')
        root.resizable(False, False)
        root.protocol("WM_DELETE_WINDOW", self.controller.on_cerrar_ventana)
        return root

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

    def definir_estilos_ttk(self):

            style_tabs = ttk.Style()
            if not style_tabs.theme_names().__contains__('medidor_acustico'):

                settings = {"TNotebook.Tab": {"configure": {"padding": [5, 2],
                                                            "background": "#fdd57e"
                                                            },
                                              "map": {"background": [("selected", "#bb3939"),
                                                                     ("active", "#fdadc7"),
                                                                     ("!disabled", "#5e0606")],
                                                      "foreground": [("selected", "#ffffff"),
                                                                     ("active", "#000000"),
                                                                     ("!disabled", "#ffffff")]

                                                      }
                                              },
                            "TNotebook": {"configure": {"background": "#831212"}
                                          }
                            }
                style_tabs.theme_create("medidor_acustico", parent="alt", settings=settings)

            style_tabs.theme_use("medidor_acustico")

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

    def refrescar(self):
        self.controller.actualizar()
        self.root.after(1000, self.refrescar)

    def bloquear_controles(self):
        self.boton_salir.config(state=DISABLED)
        self.tab_control.desactivar()

    def desbloquear_controles(self):
        self.boton_salir.config(state=NORMAL)
        self.tab_control.activar()

    def mostrar_error_lundeby(self, mensaje):
        messagebox.showerror("Error", mensaje)

    def graficar_medicion_general(self):
        tab_activa = self.get_tab_activa()
        medicion_general = self.controller.get_medicion_nivel_db()
        tab_activa.graficar(medicion_general.get_respuesta_impulsional(), medicion_general.get_curva_decaimiento())




