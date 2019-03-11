from tkinter import ttk, Frame


class TabControl:

    def __init__(self, master):
        self.master = master
        self.notebook = ttk.Notebook(master)
        self.notebook.grid(row=0, column=0, columnspan=2)
        self.tabs = {}

    def agregar_tab(self, nombre, tab, titulo_tab):
        self.tabs[nombre] = tab
        frame = Frame(self.master)
        self.notebook.add(frame, text=titulo_tab)
        return frame

