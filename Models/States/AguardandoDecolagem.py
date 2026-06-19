from Models.States.State_Aviao import StateAviao, informandoControle

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
        from Models.States.EmVoo import EmVoo
        return informandoControle(
            EmVoo(),
            "Controle → {self.__identificador}: Decolagem autorizada. Procedimento liberado.",
        )

    def pousar(self):
        return informandoControle(
            self,
            "Controle → {self.__identificador}: Operação inválida. A aeronave encontra-se em solo.",
        )

    def declararEmergencia(self):
        from Models.States.EmEmergencia import EmEmergencia
        return informandoControle(
            EmEmergencia(),
            "Controle → {self.__identificador}: Emergência registrada. Decolagem cancelada e prioridade operacional concedida.",
        )
