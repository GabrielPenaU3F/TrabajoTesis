from abc import ABC, abstractmethod


class View(ABC):

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.ventana_activa = None

    @abstractmethod
    def configurar_root(self):
        pass

    def get_vista(self):
        return self

    def mostrar_vista(self):
        self.ventana_activa = True
        self.root.after(0, self.root.deiconify)

    def ocultar_vista(self):
        self.ventana_activa = False
        self.root.withdraw()



