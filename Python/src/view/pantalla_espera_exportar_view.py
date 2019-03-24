from tkinter import Toplevel, Label, Frame
from tkinter.ttk import Progressbar

from controller.pantalla_espera_exportar_controller import PantallaEsperaExportarController
from view.view import View


class PantallaEsperaExportarView(View):

    def __init__(self):

        super().__init__(Toplevel(), PantallaEsperaExportarController(self))

        self.construir_main_frame()

        self.construir_progressbar_frame()

        self.ocultar_vista()

        self.root.after(0, self.configurar_root)

    def configurar_root(self):
        # ----- Configuracion del root ------
        self.root.title("Exportando")
        self.root.geometry("250x150")
        super(PantallaEsperaExportarView, self).configurar_root()

    def construir_progressbar_frame(self):

        self.label_progreso = Label(self.main_frame)
        self.label_progreso.config(text="Exportando", pady=20, padx=20, font=("Helvetica", 10))
        self.label_progreso.grid(row=0, column=0)

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
        super(PantallaEsperaExportarView, self).ocultar_vista()
        self.pb_frame.grid_remove()

    def mostrar_vista(self):
        self.pb_frame.grid(row=1, column=0)
        super(PantallaEsperaExportarView, self).mostrar_vista()
        self.progressbar.start(10)
