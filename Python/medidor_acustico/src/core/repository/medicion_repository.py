class MedicionRepository:

    def __init__(self):
        self.medicion = None

    def put_medicion(self, medicion):
        self.medicion = medicion

    def get_medicion(self):
        return self.medicion

    def hay_medicion(self):
        return self.medicion is not None
