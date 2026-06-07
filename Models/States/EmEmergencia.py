from Models.States.State_Aviao import StateAviao, informandoControle
from Models.States.EmEmergencia import EmEmergencia
from Models.States.Pousando import Pousando

class EmEmergencia(StateAviao):
    def solicitarPouso(self):
        return informandoControle(
            Pousando(),
            "Controle → {self.__identificador}: Pouso emergencial autorizado. Prioridade máxima concedida.",
        )

    def solicitarDecolagem(self):
        return informandoControle(
            self,
            "Controle → {self.__identificador}: Operação inválida. A aeronave encontra-se em situação de emergência.",
        )

    def decolar(self):
        return informandoControle(
            self,
            "Controle → {self.__identificador}: Operação inválida. A aeronave encontra-se em situação de emergência.",
        )

    def pousar(self):
        return informandoControle(
            self,
            "Controle → {self.__identificador}: Operação inválida. Solicite pouso emergencial antes de iniciar a aproximação.",
        )

    def declararEmergencia(self):
        return informandoControle(
            EmEmergencia(),
            "Controle → {self.__identificador}: Emergência já registrada. Prioridade máxima mantida.",
        )
