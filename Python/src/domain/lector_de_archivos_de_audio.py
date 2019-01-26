from tkinter import filedialog


class LectorDeArchivosDeAudio:

    def cargar_archivo(self):
        return filedialog.askopenfile(title="Seleccionar archivo", filetypes=(("Archivos RI", "*.ri"),
                                                                                ("Todos los archivos", "*.*")))
