from tkinter import *;

from controller.instrucciones_controller import InstruccionesController
from provider.repository_provider import RepositoryProvider


class InstruccionesView:

    def __init__(self):

        self.controller = InstruccionesController(self)

        self.string_repository = RepositoryProvider.provide_string_repository()

        self.root = self.construir_root()

        self.main_frame = self.construir_main_frame()

        self.construir_label_instrucciones()

        self.root.mainloop()

    def construir_root(self):
        root = Tk()
        # ----- Configuracion del root ------
        root.title("Instrucciones")
        root.iconbitmap("resources/icons/mic_icon.ico")
        root.tk_setPalette(background='#f4f3f3')
        root.resizable(False, False)
        return root

    def construir_main_frame(self):
        # ----- Configuracion del frame principal de la ventana -----
        main_frame = Frame(self.root)
        main_frame.config(width="200", height="300")
        main_frame.pack(fill="both", expand="True", padx=20, pady=20)
        return main_frame

    def construir_label_instrucciones(self):
        self.label_instrucciones = Label(self.main_frame)
        self.label_instrucciones.config(text=self.string_repository.get_string_instrucciones(), width=65,
                                        justify=CENTER, wraplength=400)
        self.label_instrucciones.pack()
