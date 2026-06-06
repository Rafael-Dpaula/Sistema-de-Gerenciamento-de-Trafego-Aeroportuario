from Models.States.State_Aviao import StateAviao

class EmEmergencia(StateAviao):
    def solicitarPouso(self):
        return True

    def decolar(self):
        return False

    def pousar(self):
        return False