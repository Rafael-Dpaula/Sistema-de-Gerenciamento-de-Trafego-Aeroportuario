from Models.States.State_Aviao import StateAviao, informandoControle

class SolicitandoPouso(StateAviao):
    def solicitarPouso(self):
        return informandoControle(
            self,
            "Controle → {self.__identificador}: Solicitação de pouso já registrada. Aguarde autorização.",
        )

    def solicitarDecolagem(self):
        return informandoControle(
            self,
            "Controle → {self.__identificador}: Operação inválida. A aeronave encontra-se em processo de pouso.",
        )

    def decolar(self):
        return informandoControle(
            self,
            "Controle → {self.__identificador}: Operação inválida. A aeronave encontra-se em processo de pouso.",
        )

    def pousar(self):
        from Models.States.Pousando import Pousando
        return informandoControle(
            Pousando(),
            "Controle → {self.__identificador}: Pouso autorizado. Inicie os procedimentos de aproximação.",
        )
    
    def declararEmergencia(self):
        from Models.States.EmEmergencia import EmEmergencia
        return informandoControle(
            EmEmergencia(),
            "Controle → {self.__identificador}: Emergência declarada. Prioridade máxima de pouso concedida."
        )
