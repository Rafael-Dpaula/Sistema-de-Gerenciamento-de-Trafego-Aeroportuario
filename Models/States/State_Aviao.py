from abc import ABC, abstractmethod

class StateAviao(ABC): # CLASSE STATE MÃE DO POLIMORFISMO DO STATE
    def __init__(self, state):
        self.state = state
    
    @abstractmethod
    def solicitarPouso(self):
        pass

    @abstractmethod
    def decolar(self):
        pass

    @abstractmethod
    def pousar(self):
        pass