from Models.States.State_Aviao import StateAviao, informandoControle

class SolicitandoPouso(StateAviao):
    def solicitarPouso(self):
        return informandoControle(
            self,
            f"Solicitação de pouso já registrada. Aguarde autorização.",
        )

    def solicitarDecolagem(self):
        return informandoControle(
            self,
            f"Operação inválida. A aeronave encontra-se em processo de pouso.",
        )

    def decolar(self):
        return informandoControle(
            self,
            f"Operação inválida. A aeronave encontra-se em processo de pouso.",
        )

    def pousar(self):
        from Models.States.Pousando import Pousando
        return informandoControle(
            Pousando(),
            f"Pouso autorizado. Inicie os procedimentos de aproximação.",
        )
    
    def declararEmergencia(self):
        from Models.States.EmEmergencia import EmEmergencia
        return informandoControle(
            EmEmergencia(),
            f"Emergência declarada. Prioridade máxima de pouso concedida."
        )
