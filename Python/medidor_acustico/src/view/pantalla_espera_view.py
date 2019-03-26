from tkinter import Toplevel, Label, Frame
from tkinter.ttk import Progressbar

from src.view.view import View


class PantallaEsperaView(View):

    def __init__(self, controller):

        super().__init__(Toplevel(), controller)

        self.construir_main_frame()

        self.construir_progressbar_frame()

        self.ocultar_vista()

    def configurar_root(self):
        super(PantallaEsperaView, self).configurar_root()
        self.root.geometry("250x150")

    def construir_main_frame(self):
        self.main_frame = Frame(self.root)
        self.main_frame.pack()

    def construir_progressbar_frame(self):
        self.label = Label(self.main_frame)
        self.label.config(pady=20, padx=20, font=("Helvetica", 10))
        self.label.grid(row=0, column=0)

        self.pb_frame = Frame(self.main_frame)
        self.pb_frame.config(padx=20, pady=20)
        # self.pb_frame.grid(row=1, column=0)
        self.progressbar = Progressbar(self.pb_frame)
        self.progressbar.config(mode="indeterminate", length=150)
        self.progressbar.pack()

    def ocultar_vista(self):
        self.progressbar.stop()
        super(PantallaEsperaView, self).ocultar_vista()
        self.pb_frame.grid_remove()

    def mostrar_vista(self):
        self.pb_frame.grid(row=1, column=0)
        super(PantallaEsperaView, self).mostrar_vista()
        self.progressbar.start(10)
