from threading import Thread
from tkinter import filedialog

from core.domain.archivos.dialogo_cargar_medicion import DialogoCargarMedicion
from core.domain.medicion import Medicion
from core.domain.mensaje import Mensaje
from core.domain.tiempo_reverberacion import TiempoReverberacion
from core.provider.queue_provider import QueueProvider
from exception.excepciones import IOException
from core.domain.senal_audio import SenalAudio


class LectorDeArchivosDeMedicion:

    def __init__(self):
        self.queue = QueueProvider.provide_thread_queue()

    def cargar_archivo(self):
        dialogo = DialogoCargarMedicion()
        with self.abrir_dialogo(dialogo) as archivo:

            if archivo:
                datos_string = archivo.read().decode('cp037')
                thread_medicion = Thread(target=self.parsear_datos, args=(datos_string,), daemon=True)
                thread_medicion.start()
            else:
                raise IOException("No se pudo leer el archivo indicado")

    def abrir_dialogo(self, dialogo):
        return filedialog.askopenfile(mode=dialogo.get_modo(),
                                      title=dialogo.get_titulo(),
                                      defaultextension=dialogo.get_extension_default(),
                                      filetypes=(dialogo.get_tipos_archivo()))

    def parsear_datos(self, datos_string):
        datos_separados = datos_string.split("$")
        datos_separados.pop(0)
        fs = int(datos_separados[0])
        valores_ri = self.parsear_lista_flotantes(datos_separados[1])
        valores_cd = self.parsear_lista_flotantes(datos_separados[2])
        valores_edt = self.parsear_lista_flotantes(datos_separados[3])
        valores_t20 = self.parsear_lista_flotantes(datos_separados[4])
        valores_t30 = self.parsear_lista_flotantes(datos_separados[5])
        curvatura = float(datos_separados[6])

        ri = SenalAudio(fs, valores_ri)
        cd = SenalAudio(fs, valores_cd)
        edt = self.constrruir_rt(valores_edt)
        t20 = self.constrruir_rt(valores_t20)
        t30 = self.constrruir_rt(valores_t30)

        medicion = Medicion(ri, cd, edt, t20, t30, curvatura, nivel=True)
        self.queue.put(Mensaje(destinatario="VistaPrincipal", mensaje="CargaCompleta", paquete=medicion))

    def parsear_lista_flotantes(self, string):
        valores = string.split(",")
        return [float(valor) for valor in valores]

    def constrruir_rt(self, valores_rt):
        return TiempoReverberacion(valores_rt[0], valores_rt[1], valores_rt[2])

