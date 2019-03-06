import tkinter
from tkinter import Tk, Frame, Toplevel, Label, ttk
from tkinter.ttk import Progressbar

from src.controller.pantalla_espera_controller import PantallaEsperaController


class PantallaEsperaView:

    def __init__(self):

        self.root = self.construir_root()

        self.controller = PantallaEsperaController(self)

        self.construir_main_frame()

        self.construir_progressbar_frame()

        self.root.after(0, self.root.deiconify)  # Luego de construir toda la interface, permito mostrar la ventana

        self.root.mainloop()

    def construir_root(self):
        root = Toplevel()
        root.withdraw()  # Inmediatamente después de la creación, oculto la ventana
        # ----- Configuracion del root ------
        root.title("Midiendo")
        root.iconbitmap("../resources/icons/mic_icon.ico")
        root.resizable(False, False)
        root.geometry("250x150")
        return root

    def construir_progressbar_frame(self):

        self.label_midiendo = Label(self.main_frame)
        self.label_midiendo.config(text="Midiendo. Por favor espere", pady=20, padx=20, font=("Helvetica", 10))
        self.label_midiendo.grid(row=0, column=0)

        self.pb_frame = Frame(self.main_frame)
        self.pb_frame.config(borderwidth=2, padx=20, pady=20)
        self.pb_frame.grid(row=1, column=0)
        self.progressbar = Progressbar(self.pb_frame)
        self.progressbar.config(mode="indeterminate", length=150)
        self.progressbar.pack()
        self.progressbar.start(10)


    def construir_main_frame(self):
        self.main_frame = Frame(self.root)
        self.main_frame.config()
        self.main_frame.pack(pady=10)

    def cerrar(self):
        self.root.destroy()
