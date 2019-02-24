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

