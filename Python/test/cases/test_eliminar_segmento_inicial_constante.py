import unittest

from src.core.provider.action_provider import ActionProvider


class TestEliminarSegmentoInicialConstante(unittest.TestCase):

    eliminar_segmento_inicial_constante_action = None

    @classmethod
    def setUpClass(cls):
        cls.eliminar_segmento_inicial_constante_action = ActionProvider.provide_eliminar_segmento_inicial_constante_action()

    



