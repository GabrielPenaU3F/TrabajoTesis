class InstruccionesController:

    def __init__(self, view):
        self.view = view

    def on_aceptar(self):
        self.view.root.destroy()
