from view.instrucciones_view import InstruccionesView


class MainController:

    def __init__(self, view):
        self.view = view

    def mostrar_instrucciones(self):
        InstruccionesView()
