class TiempoReverberacion:

    def __init__(self, rt, coef_correlacion, xi):
        self.rt = rt
        self.coef_correlacion = coef_correlacion
        self.xi = xi

    def get_rt(self):
        return self.rt

    def get_coef_correlacion(self):
        return self.coef_correlacion

    def get_xi(self):
        return self.xi
