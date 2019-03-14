from tkinter import ttk, Frame, DISABLED, NORMAL


class TabControl:

    def __init__(self, master):
        self.master = master
        self.notebook = ttk.Notebook(master)
        self.notebook.grid(row=0, column=0, columnspan=2)
        self.tabs = {}  # Indice en el notebook / Objeto tab

    def agregar_tab(self, tab, titulo_tab):
        frame = Frame(self.master)
        self.notebook.add(frame, text=titulo_tab)
        indice_tab = len(self.notebook.tabs()) - 1
        self.tabs[indice_tab] = tab
        return frame

    def get_tab_activa(self):
        indice_tab_activa = self.notebook.index('current')
        return self.tabs[indice_tab_activa]

    def desactivar(self):
        for tab in self.tabs.values():
            tab.desactivar()

    def activar(self):
        for tab in self.tabs.values():
            tab.activar()

    def verificar_ponderacion_A(self):
        return self.get_tab_activa().verificar_ponderacion_A()

    def graficar(self, respuesta_impulsional, curva_decaimiento):
        for tab in self.tabs.values():
            tab.graficar(respuesta_impulsional, curva_decaimiento)

    def mostrar_tiempos_de_reverberacion(self, edt, t20, t30):
        for tab in self.tabs.values():
            tab.mostrar_tiempos_de_reverberacion(edt, t20, t30)

    def mostrar_parametros_de_linealidad(self, edt, t20, t30, curvatura):
        for tab in self.tabs.values():
            tab.mostrar_parametros_de_linealidad(edt, t20, t30, curvatura)


