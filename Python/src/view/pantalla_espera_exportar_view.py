from controller.pantalla_espera_exportar_controller import PantallaEsperaExportarController
from view.pantalla_espera_view import PantallaEsperaView


class PantallaEsperaExportarView(PantallaEsperaView):

    def __init__(self):
        super().__init__(PantallaEsperaExportarController(self))

        self.configurar_label()

        self.root.after(0, self.configurar_root)

    def configurar_root(self):
        # ----- Configuracion del root ------
        super(PantallaEsperaExportarView, self).configurar_root()
        self.root.title("Exportando")

    def configurar_label(self):
        self.label.config(text="Exportando datos. Por favor espere", pady=20, padx=20, font=("Helvetica", 10))
