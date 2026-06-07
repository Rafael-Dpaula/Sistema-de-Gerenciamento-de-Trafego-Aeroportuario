from Models.States.State_Aviao import StateAviao, informandoControle
from Models.States.EmEmergencia import EmEmergencia
from Models.States.SolicitandoPouso import SolicitandoPouso

class EmVoo(StateAviao):
    def solicitarPouso(self):
        return informandoControle(
            SolicitandoPouso(),
            "Controle → {self.__identificador}: Solicitação de pouso recebida. Aguarde instruções da torre.",
        )

    def solicitarDecolagem(self):
        return informandoControle(
            self,
            "Controle → {self.__identificador}: Operação inválida. A aeronave já se encontra em voo.",
        )

    def decolar(self):
        return informandoControle(
            self,
            "Controle → {self.__identificador}: Operação inválida. A aeronave já se encontra em voo.",
        )

    def pousar(self):
        return informandoControle(
            self,
            "Controle → {self.__identificador}: Operação inválida. Solicite autorização de pouso primeiro.",
        )
        
    def declararEmergencia(self):
        return informandoControle(
            EmEmergencia(),
            "Controle → {self.__identificador}: Emergência declarada. Prioridade operacional concedida."
        )
