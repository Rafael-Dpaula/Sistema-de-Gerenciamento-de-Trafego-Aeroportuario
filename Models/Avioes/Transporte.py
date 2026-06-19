from Models.Avioes.Aviao import Aviao
from Models.States.State_Aviao import StateAviao
from Models.States import *
from Models.Observer.Observer import Observer
from Models.PlanoVoo import PlanoVoo


class Transporte(Aviao):
    def __init__(
        self,
        identificador: str,
        modelo: str,
        tipoCarga: str,
        pesoCarga: float,
        planoVoo=None,
    ):
        super().__init__(identificador, modelo, planoVoo)
        self.identificador = identificador
        self.modelo = modelo
        self.planoVoo: PlanoVoo = planoVoo
        self._observadores: list[Observer] = []
        self.tipoCarga = tipoCarga
        self.pesoCarga = pesoCarga

    @property
    def tipoCarga(self):
        return self._tipoCarga

    @property
    def pesoCarga(self):
        return self._pesoCarga

    @tipoCarga.setter
    def tipoCarga(self, novoTipo):
        if novoTipo == None:
            raise TypeError("ERROR: novaComp não é uma string válida.")
        self._tipoCarga = novoTipo

    @pesoCarga.setter
    def pesoCarga(self, novoPeso):
        if not isinstance(novoPeso, float) or novoPeso < 0:
            raise Exception("ERROR: novoPeso não é um float válido.")
        self._pesoCarga = novoPeso

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
            f"Tipo da Carga: {self._tipoCarga}\n"
            f"Peso da Carga: {self._pesoCarga}\n"
            "==========================="
        )

        return msg

