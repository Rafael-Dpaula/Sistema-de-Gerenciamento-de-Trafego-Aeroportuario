from abc import ABC, abstractmethod
class Observer(ABC):
    @abstractmethod
    def atualizar(self, origem, mensagem):
        pass