from Models.Avioes.Aviao import Aviao
from Models.States.State_Aviao import StateAviao
from Models.States import *
from Models.Observer.Observer import Observer
from Models.PlanoVoo import PlanoVoo


class Privado(Aviao):
    def __init__(
        self,
        identificador: str,
        modelo: str,
        proprietario: str,
        numeroPassageiros: int,
        planoVoo=None,
    ):
        super().__init__(identificador, modelo, planoVoo)
        self.identificador = identificador
        self.modelo = modelo
        self.planoVoo: PlanoVoo = planoVoo
        self._observadores: list[Observer] = []
        self.proprietario = proprietario
        self.numeroPassageiros = numeroPassageiros

    @property
    def proprietario(self):
        return self._proprietario

    @property
    def numeroPassageiros(self):
        return self._numeroPassageiros

    @proprietario.setter
    def proprietario(self, novaDono):
        if novaDono == None:
            raise TypeError("ERROR: novaComp não é uma string válida.")
        self._proprietario = novaDono

    @numeroPassageiros.setter
    def numeroPassageiros(self, novoNum):
        if not isinstance(novoNum, int) or novoNum < 0:
            raise Exception("ERROR: novoNum não é um inteiro válido.")
        self._numeroPassageiros = novoNum

    def __str__(self):
        msg = (
            "======== PRIVADO ========\n"
            f"ID: {self._identificador}\n"
            f"Modelo: {self._modelo}\n"
            f"Status: {type(self._status).__name__}\n"
        )

        if self._planoVoo is not None:
            msg += (
                "Plano de Voo:\n"
                f"  Origem: {self._planoVoo._origem}\n"
                f"  Destino: {self._planoVoo._destino}\n"
                f"  Horário Partida: {self._planoVoo._horarioPartida}\n"
                f"  Horário Chegada: {self._planoVoo._horarioChegada}\n"
                f"  Altitude de Cruzeiro: {self._planoVoo._altitudeCruzeiro}\n"
            )
        else:
            msg += "Plano de Voo: nenhum\n"

        msg += (
            f"Observadores: {[type(obs).__name__ for obs in self._observadores]}\n"
            f"Proprietário: {self._proprietario}\n"
            f"Número de Passageiros: {self._numeroPassageiros}\n"
            "==========================="
        )

        return msg

