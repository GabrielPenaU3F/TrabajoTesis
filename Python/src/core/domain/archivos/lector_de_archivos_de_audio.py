from tkinter import filedialog

import numpy

from src.exception.excepciones import IOException
from src.core.domain.senal_audio import SenalAudio


class LectorDeArchivosDeAudio:

    def cargar_archivo(self):
        archivo = filedialog.askopenfile(mode="rb", title="Seleccionar archivo", filetypes=(("Archivos RI", "*.ri"),
                                                                                ("Todos los archivos", "*.*")))
        if archivo:
            datos_string = archivo.read().decode('cp037')
            return self.parsear_datos(datos_string)
        else: raise IOException("No se pudo leer el archivo indicado")

    def parsear_datos(self, datos_string):
        datos_separados = datos_string.split(",")
        fs = int(datos_separados[0])
        datos = numpy.zeros(len(datos_separados) - 1)
        for i in range(len(datos)):
            datos[i] = float(datos_separados[i+1])
        return SenalAudio(fs, datos)
