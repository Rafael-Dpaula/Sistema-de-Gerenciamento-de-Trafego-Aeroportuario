from Models.States.State_Aviao import StateAviao, informandoControle
class Pousando(StateAviao):
    def solicitarPouso(self):
        return informandoControle(
            self,
            f"Operação inválida. A aeronave está em procedimento de pouso.",
        )

    def solicitarDecolagem(self):
        return informandoControle(
            self,
            f"Operação inválida. A aeronave está em procedimento de pouso.",
        )

    def decolar(self):
        return informandoControle(
            self,
            f"Operação inválida. A aeronave está em procedimento de pouso.",
        )

    def pousar(self):
        from Models.States.EmSolo import EmSolo
        return informandoControle(
            EmSolo(),
            f"Pouso concluído com sucesso.",
        )
    
    def declararEmergencia(self):
        from Models.States.EmEmergencia import EmEmergencia
        return informandoControle(
            EmEmergencia(),
            f"Emergência registrada durante a aproximação. Prioridade mantida."
        )