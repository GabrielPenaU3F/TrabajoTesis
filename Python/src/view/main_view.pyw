from tkinter import *
from src.controller.main_controller import MainController
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

class MainView:

    def __init__(self):

        self.controller = MainController(self)

        self.root = self.construir_root()

        self.main_frame = self.construir_main_frame()

        self.construir_estructura_principal()

        self.construir_frame_titulos()

        self.construir_frame_graficas()

        self.construir_frame_medicion()

        self.construir_frame_resultados()

        self.root.after(0, self.root.deiconify)  # Luego de construir toda la interface, permito mostrar la ventana

        self.root.mainloop()

    def construir_frame_resultados(self):

        # ----- Frame de resultados -----

        self.label_titulo_resultados = Label(self.frame_titulo_resultados)
        self.label_titulo_resultados.config(text="Resultados")
        self.label_titulo_resultados.pack(fill="both", expand="True", ipadx=3, ipady=3)

        self.label_edt = Label(self.frame_resultados)
        self.label_edt.config(text="EDT:")
        self.label_edt.grid(row=0, column=0)
        self.entry_edt = Entry(self.frame_resultados)
        self.entry_edt.config(relief="sunken", borderwidth=2, state=DISABLED, width=10)
        self.entry_edt.grid(row=0, column=1, padx=(10, 0))

        self.label_t20 = Label(self.frame_resultados)
        self.label_t20.config(text="T20:")
        self.label_t20.grid(row=1, column=0)
        self.entry_t20 = Entry(self.frame_resultados)
        self.entry_t20.config(relief="sunken", borderwidth=2, state=DISABLED, width=10)
        self.entry_t20.grid(row=1, column=1, padx=(10, 0))

        self.label_t30 = Label(self.frame_resultados)
        self.label_t30.config(text="T30:")
        self.label_t30.grid(row=2, column=0)
        self.entry_t30 = Entry(self.frame_resultados)
        self.entry_t30.config(relief="sunken", borderwidth=2, state=DISABLED, width=10)
        self.entry_t30.grid(row=2, column=1, padx=(10, 0))

        self.label_t60_30 = Label(self.frame_resultados)
        self.label_t60_30.config(text="T60(30):")
        self.label_t60_30.grid(row=3, column=0)
        self.entry_t60_30 = Entry(self.frame_resultados)
        self.entry_t60_30.config(relief="sunken", borderwidth=2, state=DISABLED, width=10)
        self.entry_t60_30.grid(row=3, column=1, padx=(10, 0))


    def construir_frame_medicion(self):

        # ----- Frame de medicion -----
        self.boton_instrucciones = Button(self.frame_medicion, text="Instrucciones",
                                          command=self.controller.on_mostrar_instrucciones)
        self.boton_instrucciones.grid(row=0, column=0, padx=(0, 10))

        self.boton_cargar_archivo = Button(self.frame_medicion, text="Cargar archivo", command=self.controller.on_cargar_archivo)
        self.boton_cargar_archivo.grid(row=0, column=1, padx=10)

        self.boton_medir = Button(self.frame_medicion, text="Medir", command=self.controller.on_efectuar_medicion)
        self.boton_medir.grid(row=0, column=2, padx=10)

        self.radiob_metodo_var = StringVar(value="ESS")
        self.radiob_ess = Radiobutton(self.frame_medicion, text="Método ESS", variable=self.radiob_metodo_var, value="ESS")
        self.radiob_ess.grid(row=0, column=3, padx=10)
        self.radiob_mls = Radiobutton(self.frame_medicion, text="Método MLS", variable=self.radiob_metodo_var, value="MLS")
        self.radiob_mls.grid(row=0, column=4, padx=10)

        self.boton_guardar_archivo = Button(self.frame_medicion, text="Guardar archivo", command=self.controller.on_guardar_archivo)
        self.boton_guardar_archivo.grid(row=0, column=5, padx=10)

        boton_ver_por_bandas = Button(self.frame_boton_derecha, text="Vista detallada", state=DISABLED)
        boton_ver_por_bandas.pack(padx=(10, 0))

    def construir_frame_graficas(self):

        # ----- Frame de gráficas -----

        self.frame_graf_rta_impulsional = Frame(self.frame_graficas)
        self.frame_graf_rta_impulsional.config(width=500, height=300, borderwidth=2, relief="groove")
        self.frame_graf_rta_impulsional.pack_propagate(False)
        self.frame_graf_rta_impulsional.grid(row=0, column=0)
        self.label_graf_respuesta_impulsional = Label(self.frame_graf_rta_impulsional)
        self.label_graf_respuesta_impulsional.pack()
        self.frame_toolbar_rta_impulsional = Frame(self.frame_graficas)
        self.frame_toolbar_rta_impulsional.config(width=500, height=40, borderwidth=2)
        self.frame_toolbar_rta_impulsional.pack_propagate(False)
        self.frame_toolbar_rta_impulsional.grid(row=1, column=0)
        self.construir_plot_respuesta_impulsional()


        self.frame_graf_curva_decaimiento = Frame(self.frame_graficas)
        self.frame_graf_curva_decaimiento.config(width=500, height=300, borderwidth=2, relief="groove")
        self.frame_graf_curva_decaimiento.pack_propagate(False)
        self.frame_graf_curva_decaimiento.grid(row=0, column=1)
        self.label_graf_curva_decaimiento = Label(self.frame_graf_curva_decaimiento)
        self.label_graf_curva_decaimiento.pack()
        self.frame_toolbar_curva_decaimiento = Frame(self.frame_graficas)
        self.frame_toolbar_curva_decaimiento.config(width=500, height=40, borderwidth=2)
        self.frame_toolbar_curva_decaimiento.pack_propagate(False)
        self.frame_toolbar_curva_decaimiento.grid(row=1, column=1)
        self.construir_plot_curva_decaimiento()

    def construir_plot_respuesta_impulsional(self):
        self.figura_ri = Figure(figsize=(5, 5), dpi=100)
        self.plot_ri = self.figura_ri.add_subplot(1, 1, 1)

        self.canvas_ri = FigureCanvasTkAgg(self.figura_ri, master=self.label_graf_respuesta_impulsional)
        self.canvas_ri.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(self.canvas_ri, self.frame_toolbar_rta_impulsional)
        toolbar.update()

    def construir_plot_curva_decaimiento(self):
        self.figura_cd = Figure(figsize=(5, 5), dpi=100)
        self.plot_cd = self.figura_cd.add_subplot(1, 1, 1)

        self.canvas_cd = FigureCanvasTkAgg(self.figura_cd, master=self.label_graf_curva_decaimiento)
        self.canvas_cd.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(self.canvas_cd, self.frame_toolbar_curva_decaimiento)
        toolbar.update()

    def construir_frame_titulos(self):

        # ----- Frame de títulos -----

        self.frame_titulo_rta_impulsional = Frame(self.frame_titulos)
        self.frame_titulo_rta_impulsional.config(width=500, height=20, borderwidth=2, relief="groove")
        self.frame_titulo_rta_impulsional.pack_propagate(False)
        self.frame_titulo_rta_impulsional.grid(row=0, column=0)
        self.label_titulo_rta_impulsional = Label(self.frame_titulo_rta_impulsional)
        self.label_titulo_rta_impulsional.config(text="Respuesta impulsional", background="#dfdfdf")
        self.label_titulo_rta_impulsional.pack(fill="both", expand="True", ipadx=3, ipady=3)

        self.frame_titulo_curva_decaimiento = Frame(self.frame_titulos)
        self.frame_titulo_curva_decaimiento.config(width=500, height=20, borderwidth=2, relief="groove")
        self.frame_titulo_curva_decaimiento.pack_propagate(False)
        self.frame_titulo_curva_decaimiento.grid(row=0, column=1)
        self.label_titulo_curva_decaimiento = Label(self.frame_titulo_curva_decaimiento)
        self.label_titulo_curva_decaimiento.config(text="Curva de decaimiento", background="#dfdfdf")
        self.label_titulo_curva_decaimiento.pack(fill="both", expand="True", ipadx=3, ipady=3)

    def construir_estructura_principal(self):

        # ----- Divido el frame principal en un grid de 3x2 -----

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
        self.frame_titulo_resultados.config(width=125, height=20, borderwidth=2, relief="groove")
        self.frame_titulo_resultados.pack_propagate(False)

        self.frame_resultados = Frame(self.main_frame)
        self.frame_resultados.grid(row=1, column=1, sticky="n", padx=(20, 0), pady=(20, 0))

    def construir_main_frame(self):
        # ----- Configuracion del frame principal de la ventana -----
        main_frame = Frame(self.root)
        main_frame.config(width="1200", height="600")
        main_frame.pack(fill="both", expand="True", padx=20, pady=20)
        return main_frame

    def construir_root(self):
        root = Tk()
        root.withdraw() #Inmediatamente después de la creación, oculto la ventana
        # ----- Configuracion del root ------
        root.title("Medidor Acústico por Gabriel Pena")
        root.iconbitmap("../resources/icons/mic_icon.ico")
        root.tk_setPalette(background='#f4f3f3')
        root.resizable(False, False)
        return root

    def graficar_respuesta_impulsional(self, dominio_temporal, respuesta_impulsional):
        self.plot_ri.cla()
        self.plot_ri.plot(dominio_temporal, respuesta_impulsional)
        self.canvas_ri.draw()

    def graficar_curva_decaimiento(self, dominio_temporal, curva_decaimiento):
        self.plot_cd.cla()
        self.plot_cd.plot(dominio_temporal, curva_decaimiento)
        self.canvas_cd.draw()
