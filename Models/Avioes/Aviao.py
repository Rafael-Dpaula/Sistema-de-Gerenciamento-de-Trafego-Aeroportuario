from abc import ABC, abstractmethod
from Models.States.State_Aviao import StateAviao
from Models.Observer.Observer import Observer
from Models.PlanoVoo import PlanoVoo


class Aviao(ABC):  # CLASSE PRINCIPAL DO PROJETO, CENTRO DE TODAS AS OPERAÇÕES
    def __init__(self, identificador: str, modelo: str, planoVoo=None):
        self.identificador = identificador
        self.modelo = modelo
        self.__status: StateAviao = StateAviao.Em_Solo()
        self.planoVoo: PlanoVoo = planoVoo
        self.__observadores: list[Observer] = []

    @property
    def identificador(self):
        return self.__identificador

    @property
    def modelo(self):
        return self.__modelo

    @property
    def status(self):
        return self.__status

    @property
    def planoVoo(self):
        return self.__planoVoo

    @property
    def observadores(self):
        return self.__observadores

    @identificador.setter
    def identificador(self, novoId):
        if novoId == None:
            raise TypeError("ERROR: o novoID deve ser informado.")
        self.__identificador = novoId.strip().toUpper()

    @modelo.setter
    def modelo(self, novoModelo):
        if novoModelo == None:
            raise TypeError("ERROR: o novoModelo deve ser informado.")
        self.__modelo = novoModelo.strip().toUpper()

    @planoVoo.setter
    def planoVoo(self, novoPlano):
        if not isinstance(novoPlano, PlanoVoo):
            raise TypeError(
                "ERROR: o novoPlano deve ser uma instância válida de PlanoVoo."
            )

    ###                     METODOS

    def adicionarObserver(
        self, observador
    ):  # adiciona o observador na lista de observadores do aviao
        if isinstance(
            observador, Observer
        ):  # testa se o observador pe um objeto valido
            self.__observadores.append(observador)  # coloca o observador na lista
        else:
            raise TypeError(
                "ERROR: observador não é uma instância de Observer."
            )  # exibe um erro caso o observador seja inválido

    def removerObserver(
        self, observador
    ):  # remove o observador da lista de observadores do aviao
        if (observador, Observer):  # testa se o observador é um objeto valido
            if not any(
                o == observador for o in self.__observadores
            ):  # faz uma busca se o objeto não está na lista de observadores
                print(
                    f"ALERT: o observador não foi encontrado na lista de observadores do avião."
                )
                return
            self.__observadores.remove(
                observador
            )  # remove o observador caso ele seja encontrado
        else:
            raise TypeError(
                "ERROR: observador não é uma instância de Observer."
            )  # exibe um erro caso o observador seja inválido

    def notificarObservers(self, mensagem):
        if not mensagem == None:
            for observers in self.__observadores:
                observers.atualizar(self, mensagem)

    def alterarStatus(self, estado):
        if not isinstance(
            estado, StateAviao
        ):  # verifica se estado e uma instancia valida de StateAviao
            raise TypeError("ERROR: estado não é uma instancia válida de StateAviao.")
        self.__status = estado
        self.notificarObservers(
            f"Aeronave {self.__identificador} mudou para " f"{type(estado).__name__}",
        )  # informa a mudança do status aos observadores

    def solicitarPouso(self):  # pedido da aeronave para a torre para pousar
        resultado = self.__status.solicitarPouso()
        self.alterarStatus(resultado.estado)
        return resultado.mensagem

    def solicitarDecolagem(self):  # pedido da aeronave para a torre para decolagem
        resultado = self.__status.solicitarDecolagem()
        self.alterarStatus(resultado.estado)
        return resultado.mensagem

    def pousar(self):  # informando a torre que esta pousando
        resultado = self.__status.pousar()
        self.alterarStatus(resultado.estado)
        return resultado.mensagem

    def decolar(self):  # informando a torre que esta decolando
        resultado = self.__status.decolar()
        self.alterarStatus(resultado.estado)
        return resultado.mensagem

    def declararEmergencia(
        self,
    ):  # informa a torre que a aeronave está em estado de emergencia e necessita de prioridade
        resultado = self.__status.declararEmergencia()
        self.alterarStatus(resultado.estado)
        return resultado.mensagem

    def __str__(ABC):
        pass
