from tkinter import filedialog


class EscritorDeArchivosDeAudio:

    def guardar_archivo(self):
        return filedialog.asksaveasfile(mode="w", title="Guardar archivo", filetypes=(("Archivos RI", "*.ri"),
                                                                                ("Todos los archivos", "*.*")))
