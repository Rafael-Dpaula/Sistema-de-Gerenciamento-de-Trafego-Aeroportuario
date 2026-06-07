from Models.States.State_Aviao import StateAviao, informandoControle
from Models.States.EmEmergencia import EmEmergencia
from Models.States.EmSolo import EmSolo
class Pousando(StateAviao):
    def solicitarPouso(self):
        return informandoControle(
            self,
            "Controle → {self.__identificador}: Operação inválida. A aeronave está em procedimento de pouso.",
        )

    def solicitarDecolagem(self):
        return informandoControle(
            self,
            "Controle → {self.__identificador}: Operação inválida. A aeronave está em procedimento de pouso.",
        )

    def decolar(self):
        return informandoControle(
            self,
            "Controle → {self.__identificador}: Operação inválida. A aeronave está em procedimento de pouso.",
        )

    def pousar(self):
        return informandoControle(
            EmSolo(),
            "Controle → {self.__identificador}: Pouso concluído com sucesso.",
        )
    
    def declararEmergencia(self):
        return informandoControle(
            EmEmergencia(),
            "Controle → {self.__identificador}: Emergência registrada durante a aproximação. Prioridade mantida."
        )