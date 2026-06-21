from Models.States.State_Aviao import StateAviao, informandoControle

class EmVoo(StateAviao):
    def solicitarPouso(self):
        from Models.States.SolicitandoPouso import SolicitandoPouso
        return informandoControle(
            SolicitandoPouso(),
            f"Solicitação de pouso recebida. Aguarde instruções da torre.",
        )

    def solicitarDecolagem(self):
        return informandoControle(
            self,
            f"Operação inválida. A aeronave já se encontra em voo.",
        )

    def decolar(self):
        return informandoControle(
            self,
            f"Operação inválida. A aeronave já se encontra em voo.",
        )

    def pousar(self):
        return informandoControle(
            self,
            f"Operação inválida. Solicite autorização de pouso primeiro.",
        )
        
    def declararEmergencia(self):
        from Models.States.EmEmergencia import EmEmergencia
        return informandoControle(
            EmEmergencia(),
            f"Emergência declarada. Prioridade operacional concedida."
        )
