from Models.States.State_Aviao import StateAviao, informandoControle

class EmEmergencia(StateAviao):
    def solicitarPouso(self):
        from Models.States.Pousando import Pousando
        return informandoControle(
            Pousando(),
            f"Pouso emergencial autorizado. Prioridade máxima concedida.",
        )

    def solicitarDecolagem(self):
        return informandoControle(
            self,
            f"Operação inválida. A aeronave encontra-se em situação de emergência.",
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
