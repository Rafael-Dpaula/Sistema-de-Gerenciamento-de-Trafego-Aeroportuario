from Models.States.State_Aviao import StateAviao, informandoControle

class AguardandoDecolagem(StateAviao):

    def solicitarDecolagem(self):
        return informandoControle(
            self,
            f"Solicitação já registrada. Aguarde autorização.",
        )

    def solicitarPouso(self):
        return informandoControle(
            self,
            f"Operação inválida. A aeronave encontra-se em solo.",
        )

    def decolar(self):
        from Models.States.EmVoo import EmVoo
        return informandoControle(
            EmVoo(),
            f"Decolagem autorizada. Procedimento liberado.",
        )

    def pousar(self):
        return informandoControle(
            self,
            f"Operação inválida. A aeronave encontra-se em solo.",
        )

    def declararEmergencia(self):
        from Models.States.EmEmergencia import EmEmergencia
        return informandoControle(
            EmEmergencia(),
            f"Emergência registrada. Decolagem cancelada e prioridade operacional concedida.",
        )
