from Models.States.State_Aviao import StateAviao

class EmSolo(StateAviao):
    def solicitarPouso(self):
        return False

    def decolar(self):
        return True

    def pousar(self):
        return False