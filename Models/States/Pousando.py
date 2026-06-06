from Models.States.State_Aviao import StateAviao

class Pousando(StateAviao):
    def solicitarPouso(self):
        return False

    def decolar(self):
        return False

    def pousar(self):
        return True