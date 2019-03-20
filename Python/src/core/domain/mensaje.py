class Mensaje:

    def __init__(self, destinatario, mensaje, **paquete):

        self.destinatario = destinatario
        self.mensaje = mensaje
        if paquete is not None:
            self.paquete = paquete.get('paquete')

    def get_destinatario(self):
        return self.destinatario

    def get_mensaje(self):
        return self.mensaje

    def get_paquete(self):
        if self.paquete:
            return self.paquete

