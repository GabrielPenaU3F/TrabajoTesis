from abc import abstractmethod

from controller.controller import Controller
from core.provider.repository_provider import RepositoryProvider


class PantallaConGraficasController(Controller):

    def __init__(self, view):
        super().__init__(view)
        self.binding_eventos_repository = RepositoryProvider.provide_binding_eventos_repository()
        self.root_bindings = []

    @abstractmethod
    def mostrar_error_lundeby(self):
        pass

    def bloquear_controles(self):
        self.view.bloquear_controles()

    def desbloquear_controles(self):
        self.view.desbloquear_controles()

    def bindear_eventos_root(self):
        eventos = self.binding_eventos_repository.get_eventos()
        for clave_evento in eventos:
            self.bindear_evento_root(clave_evento)

    def bindear_evento_root(self, clave_evento):
        binding = self.binding_eventos_repository.get_binding(clave_evento)
        if not self.root_bindings.__contains__(binding.get_evento()):
            self.root_bindings.append(binding.get_evento())
            self.view.bindear_evento_root(binding)

    def unbindear_evento_root(self, clave_evento):
        binding = self.binding_eventos_repository.get_binding(clave_evento)
        if self.root_bindings.__contains__(binding.get_evento()):
            self.root_bindings.remove(binding.get_evento())
            self.view.unbindear_evento_root(binding)

