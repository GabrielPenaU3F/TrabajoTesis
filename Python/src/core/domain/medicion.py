class Medicion:

    def __init__(self, respuesta_impulsional, curva_decaimiento, edt, t20, t30):
        self.respuesta_impulsional = respuesta_impulsional
        self.curva_decaimiento = curva_decaimiento
        self.edt = edt
        self.t20 = t20
        self.t30 = t30

    def get_respuesta_impulsional(self):
        return self.respuesta_impulsional

    def get_curva_decaimiento(self):
        return self.curva_decaimiento

    def get_edt(self):
        return self.edt

    def get_t20(self):
        return self.t20

    def get_t30(self):
        return self.t30
