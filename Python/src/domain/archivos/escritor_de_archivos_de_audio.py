from tkinter import filedialog

from src.exception.excepciones import IOException


class EscritorDeArchivosDeAudio:

    def guardar_archivo(self, senal):
        archivo = filedialog.asksaveasfile(mode="wb", title="Guardar archivo", defaultextension=".ri",
                                           filetypes=(("Archivos RI", ".ri"),
                                                    ("Todos los archivos", ".*")))
        if archivo:
            fs = senal.get_fs()
            valores = senal.get_valores()
            contenido = str(fs)
            for valor in valores:
                contenido += (',' + str(valor))
            archivo.write(contenido.encode('cp037'))  # IBM037 codec
            archivo.close()

        else: raise IOException("No se pudo escribir el archivo")
