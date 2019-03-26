from src.controller.pantalla_espera_medir_controller import PantallaEsperaMedirController
from src.view.pantalla_espera_view import PantallaEsperaView


class PantallaEsperaMedirView(PantallaEsperaView):

    def __init__(self):

        super().__init__(PantallaEsperaMedirController(self))

        self.configurar_label()

        self.root.after(0, self.configurar_root)

    def configurar_root(self):
        # ----- Configuracion del root ------
        super(PantallaEsperaMedirView, self).configurar_root()
        self.root.title("Midiendo")

    def configurar_label(self):
        self.label.config(text="Midiendo. Por favor espere", pady=20, padx=20, font=("Helvetica", 10))
