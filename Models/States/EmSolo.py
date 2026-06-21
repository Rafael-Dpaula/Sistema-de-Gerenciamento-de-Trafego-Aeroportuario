from Models.States.State_Aviao import StateAviao, informandoControle


class EmSolo(StateAviao):

    def solicitarDecolagem(self):
        from Models.States.AguardandoDecolagem import AguardandoDecolagem
        return informandoControle(
            AguardandoDecolagem(),
            f"Solicitação de decolagem recebida. Aguarde autorização da torre.",
        )

    def solicitarPouso(self):
        return informandoControle(
            self,
            f"Operação inválida. A aeronave já se encontra em solo.",
        )

    def decolar(self):
        return informandoControle(
            self,
            f"Operação inválida. Solicite autorização de decolagem primeiro.",
        )

    def pousar(self):
        return informandoControle(
            self,
            f"Operação inválida. A aeronave já se encontra em solo.",
        )

    def declararEmergencia(self):
        from Models.States.EmEmergencia import EmEmergencia
        return informandoControle(
            EmEmergencia(),
            f"Emergência registrada. Aguarde instruções da torre.",
        )
