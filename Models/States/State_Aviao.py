from abc import ABC, abstractmethod

class StateAviao(ABC): # CLASSE GERAL DO STATE    
    @abstractmethod
    def solicitarPouso(self):
        pass

    @abstractmethod
    def solicitarDecolagem(self):
        pass

    @abstractmethod
    def decolar(self):
        pass

    @abstractmethod
    def pousar(self):
        pass
    
    @abstractmethod
    def declararEmergencia(self):
        pass
    
class informandoControle: # classe utilizada para o retorno do estado e sua mensagem especifica
    def __init__(self, estado, mensagem):
        self.estado = estado
        self.mensagem = mensagem