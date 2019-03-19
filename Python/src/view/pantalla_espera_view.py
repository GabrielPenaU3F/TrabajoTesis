from tkinter import Frame, Toplevel, Label
from tkinter.ttk import Progressbar, Style

from src.controller.pantalla_espera_controller import PantallaEsperaController
from src.view.view import View


class PantallaEsperaView(View):

    def __init__(self):

        super().__init__(Toplevel(), PantallaEsperaController(self))

        self.controller = PantallaEsperaController(self)

        self.construir_main_frame()

        self.construir_progressbar_frame()

        self.ocultar_vista()

        self.root.after(0, self.configurar_root)

    def configurar_root(self):
        # ----- Configuracion del root ------
        self.root.title("Midiendo")
        self.root.geometry("250x150")
        super(PantallaEsperaView, self).configurar_root()

    def construir_progressbar_frame(self):

        self.label_midiendo = Label(self.main_frame)
        self.label_midiendo.config(text="Midiendo. Por favor espere", pady=20, padx=20, font=("Helvetica", 10))
        self.label_midiendo.grid(row=0, column=0)

        self.pb_frame = Frame(self.main_frame)
        self.pb_frame.config(padx=20, pady=20)
        #self.pb_frame.grid(row=1, column=0)
        self.progressbar = Progressbar(self.pb_frame)
        self.progressbar.config(mode="indeterminate", length=150)
        self.progressbar.pack()

    def construir_main_frame(self):
        self.main_frame = Frame(self.root)
        self.main_frame.pack()

    def ocultar_vista(self):
        self.progressbar.stop()
        super(PantallaEsperaView, self).ocultar_vista()
        self.pb_frame.grid_remove()

    def mostrar_vista(self):
        self.pb_frame.grid(row=1, column=0)
        super(PantallaEsperaView, self).mostrar_vista()
        self.progressbar.start(10)
