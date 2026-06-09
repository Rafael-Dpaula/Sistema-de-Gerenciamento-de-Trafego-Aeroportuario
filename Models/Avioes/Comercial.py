from Models.Avioes.Aviao import Aviao
from Models.States.State_Aviao import StateAviao
from Models.Observer.Observer import Observer
from Models.PlanoVoo import PlanoVoo


class Comercial(Aviao):
    def __init__(
        self,
        identificador: str,
        modelo: str,
        companhiaAerea: str,
        numeroPassageiros: int,
        planoVoo=None,
    ):
        super().__init__(identificador, modelo, planoVoo)
        self.identificador = identificador
        self.modelo = modelo
        self.__status: StateAviao = StateAviao.Em_Solo()
        self.planoVoo: PlanoVoo = planoVoo
        self.__observadores: list[Observer] = []
        self.companhiaAerea = companhiaAerea
        self.numeroPassageiros = numeroPassageiros

    @property
    def companhiaAerea(self):
        return self.__companhiaAerea

    @property
    def numeroPassageiros(self):
        return self.__numeroPassageiros

    @companhiaAerea.setter
    def companhiaAerea(self, novaComp):
        if novaComp == None:
            raise TypeError("ERROR: novaComp não é uma string válida.")
        self.__companhiaAerea = novaComp

    @numeroPassageiros.setter
    def numeroPassageiros(self, novoNum):
        if not isinstance(novoNum, int) or novoNum < 0:
            raise Exception("ERROR: novoNum não é um inteiro válido.")
        self.__numeroPassageiros = novoNum

    def __str__(self):

        msg = (
            "======== COMERCIAL ========\n"
            f"ID: {self.__identificador}\n"
            f"Modelo: {self.__modelo}\n"
            f"Status: {type(self.__status).__name__}\n"
        )

        if self.__planoVoo is not None:

            msg += (
                "Plano de Voo:\n"
                f"  Origem: {self.__planoVoo.__origem}\n"
                f"  Destino: {self.__planoVoo.__destino}\n"
                f"  Horário Partida: {self.__planoVoo.__horarioPartida}\n"
                f"  Horário Chegada: {self.__planoVoo.__horarioChegada}\n"
                f"  Altitude de Cruzeiro: {self.__planoVoo.__altitudeCruzeiro}\n"
            )

        else:
            msg += "Plano de Voo: nenhum\n"

        msg += (
            f"Observadores: {[type(obs).__name__ for obs in self.__observers]}\n"
            f"Companhia Aérea: {self.__companhiaAerea}\n"
            f"Número de Passageiros: {self.__numeroPassageiros}\n"
            "==========================="
        )

        return msg
