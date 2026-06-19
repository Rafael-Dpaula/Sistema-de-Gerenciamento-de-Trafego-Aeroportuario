from Models.Avioes.Aviao import Aviao
from Models.States.State_Aviao import StateAviao
from Models.States import *
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
        self.planoVoo: PlanoVoo = planoVoo
        self._observadores: list[Observer] = []
        self.companhiaAerea = companhiaAerea
        self.numeroPassageiros = numeroPassageiros

    @property
    def companhiaAerea(self):
        return self._companhiaAerea

    @property
    def numeroPassageiros(self):
        return self._numeroPassageiros

    @companhiaAerea.setter
    def companhiaAerea(self, novaComp):
        if novaComp == None:
            raise TypeError("ERROR: novaComp não é uma string válida.")
        self._companhiaAerea = novaComp

    @numeroPassageiros.setter
    def numeroPassageiros(self, novoNum):
        if not isinstance(novoNum, int) or novoNum < 0:
            raise Exception("ERROR: novoNum não é um inteiro válido.")
        self._numeroPassageiros = novoNum

    def __str__(self):
        msg = (
            "======== COMERCIAL ========\n"
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
            f"Companhia Aérea: {self._companhiaAerea}\n"
            f"Número de Passageiros: {self._numeroPassageiros}\n"
            "==========================="
        )

        return msg

