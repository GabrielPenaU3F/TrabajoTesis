from abc import ABC, abstractmethod
from tkinter import Frame, Label, BOTTOM, BOTH, StringVar, OptionMenu, BooleanVar, Checkbutton, Button, NORMAL, DISABLED
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from src.core.provider.repository_provider import RepositoryProvider


class Tab(ABC):

    def __init__(self, view, tab_control):
        self.view = view
        self.bandas_estandar_repository = RepositoryProvider.provide_bandas_estandar_repository()
        self.tab_frame = tab_control.agregar_tab(self, self.titulo_tab)
        self.construir_tab()
        
    @abstractmethod
    def obtener_bandas(self):
        pass

    def construir_tab(self):
        self.construir_frame_titulo()
        self.construir_frame_grafica()
        self.construir_frame_medicion()

    def construir_frame_titulo(self):
        self.frame_titulo_grafica = Frame(self.tab_frame)
        self.frame_titulo_grafica.config(width=400, height=20, borderwidth=2, relief="groove")
        self.frame_titulo_grafica.grid(row=0, column=0, sticky="nsew", padx=10, pady=(15, 0))
        self.label_titulo_grafica = Label(self.frame_titulo_grafica)
        self.label_titulo_grafica.config(text="Nivel de respuesta impulsional - Curva de decaimiento",
                                         bg="#0c005a")
        self.label_titulo_grafica.pack(fill="both", expand="True")

    def construir_frame_grafica(self):
        self.frame_grafica = Frame(self.tab_frame)
        self.frame_grafica.config(width=400, height=250)
        self.frame_grafica.grid(row=1, column=0, padx=10, pady=10)
        self.label_grafica = Label(self.frame_grafica)
        self.label_grafica.config(borderwidth=2, relief="groove")
        self.label_grafica.grid(row=0, column=0)
        self.frame_toolbar = Frame(self.frame_grafica)
        self.frame_toolbar.config(width=400, height=40, borderwidth=2)
        self.frame_toolbar.pack_propagate(False)
        self.frame_toolbar.grid(row=1, column=0, sticky="nsew")
        self.construir_plot()

    def construir_plot(self):
        self.figura = Figure(figsize=(6, 4), dpi=100)
        self.figura.patch.set_facecolor("#becbff")
        self.sistema_ejes = self.figura.add_subplot(1, 1, 1)
        self.sistema_ejes.set_facecolor("#dee1ec")
        self.sistema_ejes = self.limpiar_ejes(self.sistema_ejes)

        self.canvas = FigureCanvasTkAgg(self.figura, master=self.label_grafica)
        self.canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(self.canvas, self.frame_toolbar)
        toolbar.update()

    def limpiar_ejes(self, sistema_ejes):
        sistema_ejes.cla()
        sistema_ejes.set_xlabel('Tiempo (s)')
        sistema_ejes.set_ylabel('Nivel (dB)')
        sistema_ejes.set_xlim(left=0, auto=True)
        sistema_ejes.set_ylim(bottom=-120, top=0, auto=True)
        return sistema_ejes

    def construir_frame_medicion(self):
        self.frame_medicion = Frame(self.tab_frame)
        self.frame_medicion.grid(row=0, column=1, rowspan=2, sticky="n")
        self.construir_frame_bandas()

    def construir_frame_bandas(self):

        self.construir_seleccion_banda()

        self.construir_frame_rts()

        self.construir_frame_linealidad()

    def construir_seleccion_banda(self):

        self.frame_titulo_bandas = Label(self.frame_medicion)
        self.frame_titulo_bandas.config(height=20, borderwidth=2, relief="groove")
        self.frame_titulo_bandas.grid(row=0, column=0, sticky="nsew", padx=10, pady=(15, 0))
        self.label_titulo_bandas_octava = Label(self.frame_titulo_bandas)
        self.label_titulo_bandas_octava.config(text=self.titulo_bandas_text, bg="#0c005a")
        self.label_titulo_bandas_octava.pack(ipadx=10, expand="True", fill="both")
        self.frame_combobox_bandas = Frame(self.frame_medicion)
        self.frame_combobox_bandas.config(height=20, bg="#5893d4")
        self.frame_combobox_bandas.grid(row=1, column=0, sticky="nsew", padx=10, pady=(10, 0))
        bandas_estandar = self.obtener_bandas()
        self.banda_seleccionada = StringVar()
        self.banda_seleccionada.set(bandas_estandar[0])
        self.combobox_banda = OptionMenu(self.frame_combobox_bandas, self.banda_seleccionada, *bandas_estandar)
        self.combobox_banda.config(relief="groove", borderwidth=0, bg="#5893d4", activebackground="#0060ca")
        self.combobox_banda['menu'].config(bg="#5893d4", activebackground="#0060ca")
        self.combobox_banda.pack(expand="True", fill="both")
        self.checked = BooleanVar(False)
        self.ponderacion_a = Checkbutton(self.frame_medicion)
        self.ponderacion_a.config(text="Ponderación A", variable=self.checked, selectcolor="#5e0606")
        self.ponderacion_a.grid(row=2, column=0, pady=(10, 0), padx=10, sticky="w")
        self.boton_calcular = Button(self.frame_medicion)
        self.boton_calcular.config(text="Calcular", command=self.view.on_calcular, bg="#5e0606", width=20)
        self.boton_calcular.grid(row=3, column=0, pady=(20, 10))

    def construir_frame_rts(self):
        
        self.frame_titulo_rts = Label(self.frame_medicion)
        self.frame_titulo_rts.config(height=20, borderwidth=2, relief="groove")
        self.frame_titulo_rts.grid(row=4, column=0, sticky="nsew", padx=10, pady=(15, 0))
        self.label_titulo_rts = Label(self.frame_titulo_rts)
        self.label_titulo_rts.config(text="Tiempos de reverberación", bg="#0c005a")
        self.label_titulo_rts.pack(ipadx=10)

        self.frame_rts = Frame(self.frame_medicion)
        self.frame_rts.grid(row=5, column=0, padx=10, pady=(15, 0))

        self.label_edt = Label(self.frame_rts)
        self.label_edt.config(text="EDT", bg="#5893d4", borderwidth=2, relief="groove", width=4)
        self.label_edt.grid(row=0, column=0, pady=(0, 5))
        self.edt_var = StringVar()
        self.label_res_edt = Label(self.frame_rts)
        self.label_res_edt.config(relief="sunken", bg="#becbff", borderwidth=2, width=10, textvariable=self.edt_var,
                                  fg='black')
        self.label_res_edt.grid(row=0, column=1, padx=(10, 0), pady=(0, 5))
        self.label_t20 = Label(self.frame_rts)
        self.label_t20.config(text="T20", bg="#5893d4", borderwidth=2, relief="groove", width=4)
        self.label_t20.grid(row=1, column=0, pady=(0, 5))
        self.t20_var = StringVar()
        self.label_res_t20 = Label(self.frame_rts)
        self.label_res_t20.config(relief="sunken", borderwidth=2, bg="#becbff", width=10, textvariable=self.t20_var,
                                  fg='black')
        self.label_res_t20.grid(row=1, column=1, padx=(10, 0), pady=(0, 5))
        self.label_t30 = Label(self.frame_rts)
        self.label_t30.config(text="T30", bg="#5893d4", borderwidth=2, relief="groove", width=4)
        self.label_t30.grid(row=2, column=0, pady=(0, 5))
        self.t30_var = StringVar()
        self.label_res_t30 = Label(self.frame_rts)
        self.label_res_t30.config(relief="sunken", borderwidth=2, bg="#becbff", width=10, textvariable=self.t30_var,
                                  fg='black')
        self.label_res_t30.grid(row=2, column=1, padx=(10, 0), pady=(0, 5))

    def construir_frame_linealidad(self):

        self.frame_titulo_linealidad = Label(self.frame_medicion)
        self.frame_titulo_linealidad.config(height=20, borderwidth=2, relief="groove")
        self.frame_titulo_linealidad.grid(row=6, column=0, sticky="nsew", padx=10, pady=(15, 0))
        self.label_titulo_linealidad = Label(self.frame_titulo_linealidad)
        self.label_titulo_linealidad.config(text="Linealidad", bg="#0c005a")
        self.label_titulo_linealidad.pack(ipadx=10, expand="True", fill="both")

        self.frame_linealidad = Frame(self.frame_medicion)
        self.frame_linealidad.grid(row=7, column=0, padx=10, pady=(15, 0))

        self.label_r = Label(self.frame_linealidad)
        self.label_r.config(text="r", bg="#5893d4", borderwidth=2, relief="groove", width=4)
        self.label_r.grid(row=0, column=0, pady=(0, 5))
        self.r_var = StringVar()
        self.label_res_r = Label(self.frame_linealidad)
        self.label_res_r.config(relief="sunken", bg="#becbff", borderwidth=2, width=10,
                                       textvariable=self.r_var, fg='black')
        self.label_res_r.grid(row=0, column=1, padx=(10, 0), pady=(0, 5))

        self.label_xi = Label(self.frame_linealidad)
        self.label_xi.config(text="ξ", bg="#5893d4", borderwidth=2, relief="groove", width=4)
        self.label_xi.grid(row=1, column=0, pady=(0, 5))
        self.xi_var = StringVar()
        self.label_res_xi = Label(self.frame_linealidad)
        self.label_res_xi.config(relief="sunken", borderwidth=2, bg="#becbff", width=10,
                                        textvariable=self.xi_var, fg='black')
        self.label_res_xi.grid(row=1, column=1, padx=(10, 0), pady=(0, 5))

        self.label_curvatura = Label(self.frame_linealidad)
        self.label_curvatura.config(text="C", bg="#5893d4", borderwidth=2, relief="groove", width=4)
        self.label_curvatura.grid(row=2, column=0, pady=(0, 5))
        self.curvatura_var = StringVar()
        self.label_res_curvatura = Label(self.frame_linealidad)
        self.label_res_curvatura.config(relief="sunken", borderwidth=2, bg="#becbff", width=10,
                                               textvariable=self.curvatura_var, fg='black')
        self.label_res_curvatura.grid(row=2, column=1, padx=(10, 0), pady=(0, 5))

    def get_frecuencia_central_banda_seleccionada(self):
        return float(self.banda_seleccionada.get())

    def get_tipo(self):
        return self.tipo

    def desactivar(self):
        self.combobox_banda.config(state=DISABLED)
        self.ponderacion_a.config(state=DISABLED)
        self.boton_calcular.config(state=DISABLED)

    def activar(self):
        self.combobox_banda.config(state=NORMAL)
        self.ponderacion_a.config(state=DISABLED)
        self.boton_calcular.config(state=NORMAL)

    def graficar(self, nivel_respuesta_impulsional, curva_decaimiento):
        dominio_temporal_ri = nivel_respuesta_impulsional.get_dominio_temporal()
        valores_ri = nivel_respuesta_impulsional.get_valores()
        dominio_temporal_cd = curva_decaimiento.get_dominio_temporal()
        valores_cd = curva_decaimiento.get_valores()
        self.limpiar_ejes(self.sistema_ejes)
        self.sistema_ejes.plot(dominio_temporal_ri, valores_ri, color='#0000ff', linewidth=0.1)
        self.sistema_ejes.plot(dominio_temporal_cd, valores_cd, color="#ff0000", linewidth=1)
        self.canvas.draw()

    def mostrar_tiempos_de_reverberacion(self, edt, t20, t30):
        self.edt_var.set(round(edt, 4))
        self.t20_var.set(round(t20, 4))
        self.t30_var.set(round(t30, 4))

