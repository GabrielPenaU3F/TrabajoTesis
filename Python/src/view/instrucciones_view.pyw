from tkinter import *

from controller.instrucciones_controller import InstruccionesController
from core.provider.repository_provider import RepositoryProvider
from view.view import View


class InstruccionesView(View):

    def __init__(self):

        super().__init__(Toplevel(), InstruccionesController(self))

        self.string_repository = RepositoryProvider.provide_string_repository()

        self.main_frame = self.construir_main_frame()

        self.construir_label_instrucciones()

        self.construir_boton_aceptar()

        self.ocultar_vista()

        self.root.after(0, self.configurar_root)

    def configurar_root(self):
        # ----- Configuracion del root ------
        self.root.title("Instrucciones")
        super(InstruccionesView, self).configurar_root()

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
        self.label_instrucciones.grid(row=0, column=0)

    def construir_boton_aceptar(self):
        self.boton_aceptar = Button(self.main_frame)
        self.boton_aceptar.config(text="Aceptar", command=self.controller.on_aceptar, bg="#5e0606")
        self.boton_aceptar.grid(row=1, column=0, pady=(20, 0))

