from Models.Avioes.Aviao import Aviao
from Models.States.State_Aviao import StateAviao
from Models.Observer.Observer import Observer
from Models.PlanoVoo import PlanoVoo


class Privado(Aviao):
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
        self.__status: StateAviao = StateAviao.Em_Solo()
        self.planoVoo: PlanoVoo = planoVoo
        self.__observadores: Observer = []
        self.tipoCarga = tipoCarga
        self.pesoCarga = pesoCarga

    @property
    def tipoCarga(self):
        return self.__tipoCarga

    @property
    def pesoCarga(self):
        return self.__pesoCarga

    @tipoCarga.setter
    def tipoCarga(self, novoTipo):
        if novoTipo == None:
            raise TypeError("ERROR: novaComp não é uma string válida.")
        self.__tipoCarga = novoTipo

    @pesoCarga.setter
    def pesoCarga(self, novoPeso):
        if not isinstance(novoPeso, float) or novoPeso < 0:
            raise Exception("ERROR: novoPeso não é um float válido.")
        self.__pesoCarga = novoPeso

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
            f"Tipo da Carga: {self.__tipoCarga}\n"
            f"Peso da Carga: {self.__pesoCarga}\n"
            "==========================="
        )

        return msg
