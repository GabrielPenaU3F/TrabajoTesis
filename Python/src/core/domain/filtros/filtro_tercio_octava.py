from core.domain.filtros.filtro_banda import FiltroBanda


class FiltroTercioOctava(FiltroBanda):

    def __init__(self, f_central):
        super().__init__()
        self.banda = self.bandas_estandar_repository.get_banda_tercio_octava(f_central)

    def get_banda(self):
        return self.banda
