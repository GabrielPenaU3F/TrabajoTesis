from tkinter import *
from src.controller.instrucciones_vista_detallada_controller import InstruccionesVistaDetalladaController
from src.core.provider.repository_provider import RepositoryProvider


class InstruccionesVistaDetalladaView:

    def __init__(self):

        self.controller = InstruccionesVistaDetalladaController(self)

        self.string_repository = RepositoryProvider.provide_string_repository()

        self.root = self.construir_root()

        self.main_frame = self.construir_main_frame()

        self.construir_label_instrucciones()

        self.construir_boton_aceptar()

        self.root.after(0, self.root.deiconify)  # Luego de construir toda la interface, permito mostrar la ventana

        self.root.mainloop()

    def construir_root(self):
        root = Toplevel()
        root.withdraw()  # Inmediatamente despues de la creación, oculto la ventana
        # ----- Configuracion del root ------
        root.title("Instrucciones")
        root.iconbitmap("../resources/icons/mic_icon.ico")
        root.resizable(False, False)
        root.protocol("WM_DELETE_WINDOW", self.controller.on_cerrar_ventana)
        return root

    def construir_main_frame(self):
        # ----- Configuracion del frame principal de la ventana -----
        main_frame = Frame(self.root)
        main_frame.config(width="200", height="300")
        main_frame.pack(fill="both", expand="True", padx=20, pady=20)
        return main_frame

    def construir_label_instrucciones(self):
        self.label_instrucciones = Label(self.main_frame)
        self.label_instrucciones.config(text=self.string_repository.get_string_instrucciones_vista_detallada(),
                                        width=65, justify=CENTER, wraplength=400)
        self.label_instrucciones.grid(row=0, column=0)

    def construir_boton_aceptar(self):
        self.boton_aceptar = Button(self.main_frame)
        self.boton_aceptar.config(text="Aceptar", command=self.controller.on_aceptar, bg="#5e0606")
        self.boton_aceptar.grid(row=1, column=0, pady=(20, 0))
