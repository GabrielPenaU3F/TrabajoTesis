from abc import ABC, abstractmethod
from tkinter import Image
import sys

from src.core.domain.estilista import Estilista


class View(ABC):

    def __init__(self, root, controller):
        self.root = root
        Estilista().definir_fuentes(root)
        self.controller = controller
        self.ventana_activa = None

    @abstractmethod
    def configurar_root(self):
        if sys.platform.startswith('win'): 
            self.root.iconbitmap('medidor_acustico/resources/icons/mic_icon.ico')
        else:
            mic = Image('photo', file='medidor_acustico/resources/icons/mic_icon.png')
            self.root.tk.call('wm', 'iconphoto', self.root._w, mic)
        self.root.tk_setPalette(background='#831212')
        self.root.resizable(False, False)
        self.root.protocol('WM_DELETE_WINDOW', self.controller.on_cerrar_ventana)

    def get_vista(self):
        return self

    def mostrar_vista(self):
        self.ventana_activa = True
        self.root.after(0, self.root.deiconify)

    def ocultar_vista(self):
        self.ventana_activa = False
        self.root.withdraw()



