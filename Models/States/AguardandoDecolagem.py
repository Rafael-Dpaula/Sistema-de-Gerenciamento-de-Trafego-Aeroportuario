from Models.States.State_Aviao import StateAviao, informandoControle
from Models.States.EmEmergencia import EmEmergencia
from Models.States.EmVoo import EmVoo

class AguardandoDecolagem(StateAviao):

    def solicitarDecolagem(self):
        return informandoControle(
            self,
            "Controle → {self.__identificador}: Solicitação já registrada. Aguarde autorização.",
        )

    def solicitarPouso(self):
        return informandoControle(
            self,
            "Controle → {self.__identificador}: Operação inválida. A aeronave encontra-se em solo.",
        )

    def decolar(self):
        return informandoControle(
            EmVoo,
            "Controle → {self.__identificador}: Decolagem autorizada. Procedimento liberado.",
        )

    def pousar(self):
        return informandoControle(
            self,
            "Controle → {self.__identificador}: Operação inválida. A aeronave encontra-se em solo.",
        )

    def declararEmergencia(self):
        return informandoControle(
            EmEmergencia,
            "Controle → {self.__identificador}: Emergência registrada. Decolagem cancelada e prioridade operacional concedida.",
        )
