from tkinter import Tk

from core.domain.coordinador_de_vistas import CoordinadorDeVistas
from core.domain.estilista import Estilista


class TkRoot:

    def __init__(self):

        root = Tk()
        root.overrideredirect(True)
        root.withdraw()

        estilista = Estilista()
        estilista.definir_estilos_ttk()
        estilista.definir_estilos_graficas()

        CoordinadorDeVistas.desplegar_vistas()

        root.mainloop()
