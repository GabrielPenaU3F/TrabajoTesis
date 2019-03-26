from src.controller.controller import Controller


class PantallaEsperaController(Controller):

    def __init__(self, view, subject):
        super().__init__(view)
        self.pantalla_espera_subject = subject
        self.pantalla_espera_subject.subscribe(on_next=lambda mensaje: self.procesar(mensaje))

