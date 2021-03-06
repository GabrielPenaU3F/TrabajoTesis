from tkinter import *
from tkinter import messagebox
from src.controller.main_controller import MainController
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from src.view.view_con_graficas import ViewConGraficas


class MainView(ViewConGraficas):

    def __init__(self):

        super().__init__(MainController(self), Toplevel())

        self.master = "VistaPrincipal"

        self.main_frame = self.construir_main_frame()

        self.construir_estructura_principal()

        self.construir_frame_titulos()

        self.construir_frame_graficas()

        self.construir_frame_medicion()

        self.construir_frame_resultados()

        self.ocultar_vista()

        self.root.after(0, self.bindear_eventos_root)

        self.root.after(0, self.configurar_root())

        self.refrescar()

    def construir_frame_resultados(self):

        # ----- Frame de resultados -----

        self.label_titulo_resultados = Label(self.frame_titulo_resultados)
        self.label_titulo_resultados.config(text="Tiempos de reverberación", bg="#0c005a")
        self.label_titulo_resultados.pack(fill="both", expand="True")

        self.label_edt = Label(self.frame_resultados)
        self.label_edt.config(text="EDT", bg="#5893d4", borderwidth=2, relief="groove", width=4)
        self.label_edt.grid(row=0, column=0, pady=(0, 5))
        self.edt_var = StringVar()
        self.label_res_edt = Label(self.frame_resultados)
        self.label_res_edt.config(relief="sunken", bg="#becbff", borderwidth=2, width=10, textvariable=self.edt_var,
                                  fg="#000001")
        self.label_res_edt.grid(row=0, column=1, padx=(10, 0), pady=(0, 5))

        self.label_t20 = Label(self.frame_resultados)
        self.label_t20.config(text="T20", bg="#5893d4", borderwidth=2, relief="groove", width=4)
        self.label_t20.grid(row=1, column=0, pady=(0, 5))
        self.t20_var = StringVar()
        self.label_res_t20 = Label(self.frame_resultados)
        self.label_res_t20.config(relief="sunken", borderwidth=2, bg="#becbff", width=10, textvariable=self.t20_var,
                                  fg="#000001")
        self.label_res_t20.grid(row=1, column=1, padx=(10, 0), pady=(0, 5))

        self.label_t30 = Label(self.frame_resultados)
        self.label_t30.config(text="T30", bg="#5893d4", borderwidth=2, relief="groove", width=4)
        self.label_t30.grid(row=2, column=0, pady=(0, 5))
        self.t30_var = StringVar()
        self.label_res_t30 = Label(self.frame_resultados)
        self.label_res_t30.config(relief="sunken", borderwidth=2, bg="#becbff", width=10, textvariable=self.t30_var,
                                  fg="#000001")
        self.label_res_t30.grid(row=2, column=1, padx=(10, 0), pady=(0, 5))



    def construir_frame_medicion(self):

        # ----- Frame de medicion -----
        self.boton_instrucciones = Button(self.frame_medicion)
        self.boton_instrucciones.config(text="Instrucciones", command=self.controller.on_mostrar_instrucciones,
                                        bg="#5e0606")
        self.boton_instrucciones.grid(row=0, column=0, padx=(0, 10))

        self.boton_cargar_archivo = Button(self.frame_medicion)
        self.boton_cargar_archivo.config(text="Cargar archivo", command=self.controller.on_cargar_archivo,
                                         bg="#5e0606")
        self.boton_cargar_archivo.grid(row=0, column=1, padx=10)

        self.boton_medir = Button(self.frame_medicion)
        self.boton_medir.config(text="Medir", command=self.controller.on_efectuar_medicion, bg="#5e0606")
        self.boton_medir.grid(row=0, column=2, padx=10)

        self.radiob_metodo_var = StringVar(value="ESS")
        self.radiob_ess = Radiobutton(self.frame_medicion)
        self.radiob_ess.config(text="Método ESS", variable=self.radiob_metodo_var, value="ESS", selectcolor="#5e0606")
        self.radiob_ess.grid(row=0, column=3, padx=10)
        self.radiob_mls = Radiobutton(self.frame_medicion)
        self.radiob_mls.config(text="Método MLS", variable=self.radiob_metodo_var, value="MLS", selectcolor="#5e0606")
        self.radiob_mls.grid(row=0, column=4, padx=10)

        self.boton_guardar_archivo = Button(self.frame_medicion)
        self.boton_guardar_archivo.config(text="Guardar archivo", command=self.controller.on_guardar_archivo,
                                          bg="#5e0606", state=DISABLED)
        self.boton_guardar_archivo.grid(row=0, column=5, padx=10)

        self.boton_exportar = Button(self.frame_medicion)
        self.boton_exportar.config(text="Exportar", command=self.controller.on_exportar, bg="#5e0606", state=DISABLED)
        self.boton_exportar.grid(row=0, column=6, padx=10)

        self.boton_vista_detallada = Button(self.frame_boton_derecha)
        self.boton_vista_detallada.config(text="Vista detallada", bg="#5e0606",
                                          command=self.controller.on_abrir_vista_detallada, state=DISABLED)
        self.boton_vista_detallada.pack(padx=(10, 0))

    def construir_frame_graficas(self):

        # ----- Frame de gráficas -----

        self.frame_graf_rta_impulsional = Frame(self.frame_graficas)
        self.frame_graf_rta_impulsional.config(width=600, height=400, borderwidth=2, relief="groove")
        self.frame_graf_rta_impulsional.pack_propagate(False)
        self.frame_graf_rta_impulsional.grid(row=0, column=0, pady=(10, 0), ipady=15)
        self.label_graf_respuesta_impulsional = Label(self.frame_graf_rta_impulsional)
        self.label_graf_respuesta_impulsional.config(bg="#5893d4")
        self.label_graf_respuesta_impulsional.pack(expand="True", fill="both")
        self.frame_toolbar_rta_impulsional = Frame(self.frame_graficas)
        self.frame_toolbar_rta_impulsional.config(width=600, height=40, borderwidth=2)
        self.frame_toolbar_rta_impulsional.pack_propagate(False)
        self.frame_toolbar_rta_impulsional.grid(row=1, column=0)
        self.construir_plot_respuesta_impulsional()

        self.frame_graf_curva_decaimiento = Frame(self.frame_graficas)
        self.frame_graf_curva_decaimiento.config(width=600, height=400, borderwidth=2, relief="groove")
        self.frame_graf_curva_decaimiento.pack_propagate(False)
        self.frame_graf_curva_decaimiento.grid(row=0, column=1, pady=(10, 0), ipady=15)
        self.label_graf_curva_decaimiento = Label(self.frame_graf_curva_decaimiento)
        self.label_graf_curva_decaimiento.config(bg="#5893d4")
        self.label_graf_curva_decaimiento.pack(expand="True", fill="both")
        self.frame_toolbar_curva_decaimiento = Frame(self.frame_graficas)
        self.frame_toolbar_curva_decaimiento.config(width=600, height=40, borderwidth=2)
        self.frame_toolbar_curva_decaimiento.pack_propagate(False)
        self.frame_toolbar_curva_decaimiento.grid(row=1, column=1)
        self.construir_plot_curva_decaimiento()

    def construir_plot_respuesta_impulsional(self):
        self.figura_ri = Figure(figsize=(10, 10), dpi=100)
        self.figura_ri.patch.set_facecolor("#becbff")
        self.sistema_ejes_ri = self.figura_ri.add_subplot(1, 1, 1)
        self.sistema_ejes_ri.set_facecolor("#dee1ec")
        self.generar_ejes_ri_limpios()

        self.canvas_ri = FigureCanvasTkAgg(self.figura_ri, master=self.label_graf_respuesta_impulsional)
        self.canvas_ri.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(self.canvas_ri, self.frame_toolbar_rta_impulsional)
        toolbar.update()

    def construir_plot_curva_decaimiento(self):
        self.figura_cd = Figure(figsize=(10, 10), dpi=100)
        self.figura_cd.patch.set_facecolor("#becbff")
        self.sistema_ejes_cd = self.figura_cd.add_subplot(1, 1, 1)
        self.sistema_ejes_cd.set_facecolor("#dee1ec")
        self.generar_ejes_cd_limpios()

        self.canvas_cd = FigureCanvasTkAgg(self.figura_cd, master=self.label_graf_curva_decaimiento)
        self.canvas_cd.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(self.canvas_cd, self.frame_toolbar_curva_decaimiento)
        toolbar.update()

    def construir_frame_titulos(self):

        # ----- Frame de títulos -----

        self.frame_titulo_rta_impulsional = Frame(self.frame_titulos)
        self.frame_titulo_rta_impulsional.config(width=600, height=20, borderwidth=2, relief="groove")
        self.frame_titulo_rta_impulsional.pack_propagate(False)
        self.frame_titulo_rta_impulsional.grid(row=0, column=0)
        self.label_titulo_rta_impulsional = Label(self.frame_titulo_rta_impulsional)
        self.label_titulo_rta_impulsional.config(text="Respuesta impulsional", background="#0c005a")
        self.label_titulo_rta_impulsional.pack(fill="both", expand="True", ipadx=3, ipady=3)

        self.frame_titulo_curva_decaimiento = Frame(self.frame_titulos)
        self.frame_titulo_curva_decaimiento.config(width=600, height=20, borderwidth=2, relief="groove")
        self.frame_titulo_curva_decaimiento.pack_propagate(False)
        self.frame_titulo_curva_decaimiento.grid(row=0, column=1)
        self.label_titulo_curva_decaimiento = Label(self.frame_titulo_curva_decaimiento)
        self.label_titulo_curva_decaimiento.config(text="Curva de decaimiento", background="#0c005a")
        self.label_titulo_curva_decaimiento.pack(fill="both", expand="True", ipadx=3, ipady=3)

    def construir_estructura_principal(self):

        self.frame_titulos = Frame(self.main_frame)
        self.frame_titulos.grid(row=0, column=0)

        self.frame_graficas = Frame(self.main_frame)
        self.frame_graficas.grid(row=1, column=0)

        self.frame_medicion = Frame(self.main_frame)
        self.frame_medicion.grid(row=2, column=0, sticky="w", pady=(10, 0))

        self.frame_boton_derecha = Frame(self.main_frame)
        self.frame_boton_derecha.grid(row=2, column=1, sticky="e")

        self.frame_titulo_resultados = Frame(self.main_frame)
        self.frame_titulo_resultados.grid(row=0, column=1, sticky="n", padx=(20, 0))
        self.frame_titulo_resultados.config(width=160, height=20, borderwidth=2, relief="groove")
        self.frame_titulo_resultados.pack_propagate(False)

        self.frame_resultados = Frame(self.main_frame)
        self.frame_resultados.grid(row=1, column=1, sticky="n", padx=(20, 0), pady=(10, 0))

    def construir_main_frame(self):
        # ----- Configuracion del frame principal de la ventana -----
        main_frame = Frame(self.root)
        main_frame.config(width="1800", height="900")
        main_frame.pack(fill="both", expand="True", padx=20, pady=20)
        return main_frame

    def configurar_root(self):
        # ----- Configuracion del root ------
        self.root.title("Medidor Acústico por Gabriel Pena")
        super(MainView, self).configurar_root()

    def graficar_respuesta_impulsional(self, dominio_temporal, respuesta_impulsional):
        self.generar_ejes_ri_limpios()
        self.sistema_ejes_ri.plot(dominio_temporal, respuesta_impulsional, color="#ff0000", linewidth=0.5)
        self.canvas_ri.draw()

    def graficar_curva_decaimiento(self, dominio_temporal, curva_decaimiento):
        self.generar_ejes_cd_limpios()
        self.sistema_ejes_cd.plot(dominio_temporal, curva_decaimiento, color="#ff0000")
        self.canvas_cd.draw()

    def mostrar_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

    def mostrar_tiempos_de_reverberacion(self, edt, t20, t30):
        self.edt_var.set(str(round(edt, 4)) + "seg")
        self.t20_var.set(str(round(t20, 4)) + "seg")
        self.t30_var.set(str(round(t30, 4)) + "seg")

    def after(self, tiempo, funcion):
        self.root.after(tiempo, funcion)

    def bloquear_controles(self):
        self.boton_cargar_archivo.config(state=DISABLED)
        self.boton_guardar_archivo.config(state=DISABLED)
        self.boton_exportar.config(state=DISABLED)
        self.boton_medir.config(state=DISABLED)
        self.boton_vista_detallada.config(state=DISABLED)
        self.radiob_ess.config(state=DISABLED)
        self.radiob_mls.config(state=DISABLED)

    def desbloquear_controles(self):
        self.boton_cargar_archivo.config(state=NORMAL)
        self.boton_medir.config(state=NORMAL)
        self.radiob_ess.config(state=NORMAL)
        self.radiob_mls.config(state=NORMAL)
        if self.controller.hay_medicion():
            self.boton_guardar_archivo.config(state=NORMAL)
            self.boton_exportar.config(state=NORMAL)
            self.boton_vista_detallada.config(state=NORMAL)

    def generar_ejes_ri_limpios(self):
        self.sistema_ejes_ri.cla()
        self.sistema_ejes_ri.set_xlabel('Tiempo (s)')
        self.sistema_ejes_ri.set_ylabel('Amplitud (V)')
        self.sistema_ejes_ri.set_xlim(left=0, auto=True)

    def generar_ejes_cd_limpios(self):
        self.sistema_ejes_cd.cla()
        self.sistema_ejes_cd.set_xlabel('Tiempo (s)')
        self.sistema_ejes_cd.set_ylabel('Nivel (dB)')
        self.sistema_ejes_cd.set_xlim(left=0, auto=True)
        self.sistema_ejes_cd.set_ylim(bottom=-120, top=0, auto=True)

    def desactivar_boton_instrucciones(self):
        self.boton_instrucciones.config(command="")

    def activar_boton_instrucciones(self):
        self.boton_instrucciones.config(command=self.controller.on_mostrar_instrucciones)

    def desactivar_boton_vista_detallada(self):
        self.boton_vista_detallada.config(command="")

    def activar_boton_vista_detallada(self):
        self.boton_vista_detallada.config(command=self.controller.on_abrir_vista_detallada)

    def redibujar_canvas(self):
        self.canvas_ri.draw()
        self.canvas_cd.draw()
        self.canvas_ri.get_tk_widget().pack()
        self.canvas_cd.get_tk_widget().pack()
        self.solicitud_de_redibujo = False

    def ocultar_graficas(self):
        self.canvas_ri.get_tk_widget().pack_forget()
        self.canvas_cd.get_tk_widget().pack_forget()
        self.solicitud_de_redibujo = True


