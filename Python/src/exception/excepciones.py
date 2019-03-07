class ValidacionParametrosSenalException(Exception):

    def __init__(self, message):
        super().__init__(message)


class CantidadDeParametrosException(Exception):

    def __init__(self, message):
        super().__init__(message)


class IOException(Exception):

    def __init__(self, message):
        super().__init__(message)


class AlineacionException(Exception):

    def __init__(self, message):
        super().__init__(message)


class FiltradoImposibleException(Exception):

    def __init__(self, message):
        super().__init__(message)


class RegresionException(Exception):

    def __init__(self, message):
        super().__init__(message)


class IndiceSenalException(Exception):

    def __init__(self, message):
        super().__init__(message)


class LundebyException(Exception):

    def __init__(self, message):
        super().__init__(message)


class FiltroException(Exception):

    def __init__(self, message):
        super().__init__(message)

