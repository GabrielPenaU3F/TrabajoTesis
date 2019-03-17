from tkinter import Frame, Toplevel, Label
from tkinter.ttk import Progressbar

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
        self.root.iconbitmap("../resources/icons/mic_icon.ico")
        self.root.resizable(False, False)
        self.root.geometry("250x150")

    def construir_progressbar_frame(self):

        self.label_midiendo = Label(self.main_frame)
        self.label_midiendo.config(text="Midiendo. Por favor espere", pady=20, padx=20, font=("Helvetica", 10))
        self.label_midiendo.grid(row=0, column=0)

        self.pb_frame = Frame(self.main_frame)
        self.pb_frame.config(borderwidth=2, padx=20, pady=20)
        self.pb_frame.grid(row=1, column=0)
        self.progressbar = Progressbar(self.pb_frame)
        self.progressbar.config(mode="indeterminate", length=150)
        self.progressbar.pack()
        self.progressbar.start(10)

    def construir_main_frame(self):
        self.main_frame = Frame(self.root)
        self.main_frame.config()
        self.main_frame.pack(pady=10)

    def ocultar_vista(self):
        self.progressbar.stop()
        super(PantallaEsperaView, self).ocultar_vista()

    def mostrar_vista(self):
        self.progressbar.start(10)
        super(PantallaEsperaView, self).mostrar_vista()
