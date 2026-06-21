from Models.States.State_Aviao import StateAviao, informandoControle


class Decolando(StateAviao):

    def solicitarDecolagem(self):
        return informandoControle(
            self,
            f"Operação inválida. A aeronave já se encontra em processo de decolagem.",
        )

    def solicitarPouso(self):
        return informandoControle(
            self,
            f"Operação inválida. A aeronave encontra-se em processo de decolagem.",
        )

    def decolar(self):
        from Models.States.EmVoo import EmVoo
        return informandoControle(
            EmVoo(),
            f"decolagem realizada com sucesso.",
        )

    def pousar(self):
        return informandoControle(
            self,
            f"Operação inválida. A aeronave encontra-se em processo de decolagem.",
        )

    def declararEmergencia(self):
        from Models.States.EmEmergencia import EmEmergencia
        return informandoControle(
            EmEmergencia(),
            f"Emergência registrada. Aguarde instruções da torre.",
        )
