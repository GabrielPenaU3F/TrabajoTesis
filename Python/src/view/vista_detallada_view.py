from tkinter import Toplevel, Frame

from src.controller.vista_detallada_controller import VistaDetalladaController


class VistaDetalladaView:

    def __init__(self):

        self.controller = VistaDetalladaController(self)

        self.root = self.construir_root()

        self.main_frame = self.construir_main_frame()

        self.construir_estructura_principal()

        self.root.after(0, self.root.deiconify)  # Luego de construir toda la interface, permito mostrar la ventana

        self.root.mainloop()

    def construir_root(self):
        root = Toplevel()
        root.withdraw()  # Inmediatamente después de la creación, oculto la ventana
        # ----- Configuracion del root ------
        root.title("Medidor Acústico - Vista detallada")
        root.iconbitmap("../resources/icons/mic_icon.ico")
        root.tk_setPalette(background='#831212')
        root.resizable(False, False)
        root.protocol("WM_DELETE_WINDOW", self.controller.on_cerrar_ventana)
        return root

    def construir_main_frame(self):
        main_frame = Frame(self.root)
        main_frame.config(width="700", height="700")
        main_frame.pack(fill="both", expand="True", padx=20, pady=20)
        return main_frame

    def construir_estructura_principal(self):
        pass
