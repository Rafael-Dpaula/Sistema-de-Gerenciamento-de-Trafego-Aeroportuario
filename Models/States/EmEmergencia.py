from Models.States.State_Aviao import StateAviao, informandoControle

class EmEmergencia(StateAviao):
    def solicitarPouso(self):
        from Models.States.SolicitandoPouso import SolicitandoPouso
        return informandoControle(
            SolicitandoPouso(),
            f"Pouso emergencial autorizado. Prioridade máxima concedida.",
        )

    def solicitarDecolagem(self):
        from Models.States.AguardandoDecolagem import AguardandoDecolagem
        return informandoControle(
            AguardandoDecolagem(),
            f"Problemas solucionados, liberado para decolagem.",
        )

    def decolar(self):
        return informandoControle(
            self,
            f"Operação inválida. A aeronave encontra-se em situação de emergência.",
        )

    def pousar(self):
        return informandoControle(
            self,
            f"Operação inválida. Solicite pouso emergencial antes de iniciar a aproximação.",
        )

    def declararEmergencia(self):
        from Models.States.EmEmergencia import EmEmergencia
        return informandoControle(
            EmEmergencia(),
            f"Emergência já registrada. Prioridade máxima mantida.",
        )
