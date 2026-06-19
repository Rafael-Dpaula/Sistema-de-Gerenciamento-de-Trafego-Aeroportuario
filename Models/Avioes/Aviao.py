from abc import ABC
from Models.States.State_Aviao import StateAviao
from Models.States.EmSolo import EmSolo

from Models.Observer.Observer import Observer
from Models.PlanoVoo import PlanoVoo



class Aviao(ABC):  # CLASSE PRINCIPAL DO PROJETO, CENTRO DE TODAS AS OPERAÇÕES
    def __init__(self, identificador: str, modelo: str, planoVoo=None):
        self.identificador = identificador
        self.modelo = modelo
        self._status: StateAviao = EmSolo()
        self.planoVoo: PlanoVoo = planoVoo
        self._observadores: list[Observer] = []

    @property
    def identificador(self):
        return self._identificador

    @property
    def modelo(self):
        return self._modelo

    @property
    def status(self):
        return self._status

    @property
    def planoVoo(self):
        return self._planoVoo

    @property
    def observadores(self):
        return self._observadores

    @identificador.setter
    def identificador(self, novoId):
        if novoId == None:
            raise TypeError("ERROR: o novoID deve ser informado.")
        self._identificador = novoId.strip().upper()

    @modelo.setter
    def modelo(self, novoModelo):
        if novoModelo == None:
            raise TypeError("ERROR: o novoModelo deve ser informado.")
        self._modelo = novoModelo.strip().upper()

    @planoVoo.setter
    def planoVoo(self, novoPlano):
        if novoPlano is not None and not isinstance(novoPlano, PlanoVoo):
            raise TypeError(
                "ERROR: o novoPlano deve ser uma instância válida de PlanoVoo."
            )
        self._planoVoo = novoPlano
        
    ### METODOS

    def definirPlano(self, plano : PlanoVoo):
        if plano is None or not isinstance(plano, PlanoVoo):
            raise TypeError("ERROR: plano de voo inválido.")
        self._planoVoo = plano
        print(f"Aeronave {self._identificador} definiu o plano de voo para {plano._destino}. Tempo de viagem estimada: {plano.calcularDuracao()}.")
        
    def adicionarObserver(
        self, observador
    ):  # adiciona o observador na lista de observadores do aviao
        if isinstance(
            observador, Observer
        ):  # testa se o observador pe um objeto valido
            self._observadores.append(observador)  # coloca o observador na lista
        else:
            raise TypeError(
                "ERROR: observador não é uma instância de Observer."
            )  # exibe um erro caso o observador seja inválido

    def removerObserver(
        self, observador
    ):  # remove o observador da lista de observadores do aviao
        if (observador, Observer):  # testa se o observador é um objeto valido
            if not any(
                o == observador for o in self._observadores
            ):  # faz uma busca se o objeto não está na lista de observadores
                print(
                    f"ALERT: o observador não foi encontrado na lista de observadores do avião."
                )
                return
            self._observadores.remove(
                observador
            )  # remove o observador caso ele seja encontrado
        else:
            raise TypeError(
                "ERROR: observador não é uma instância de Observer."
            )  # exibe um erro caso o observador seja inválido

    def notificarObservers(self, mensagem):
        if not mensagem == None:
            for observers in self._observadores:
                observers.atualizar(self, mensagem)

    def alterarStatus(self, estado):
        if not isinstance(
            estado, StateAviao
        ):  # verifica se estado e uma instancia valida de StateAviao
            raise TypeError("ERROR: estado não é uma instancia válida de StateAviao.")
        self._status = estado
        msg = f"Aeronave {self._identificador} mudou para " f"{type(estado).__name__}"
        self.notificarObservers(msg)  # informa a mudança do status aos observadores

    def solicitarPouso(self):  # pedido da aeronave para a torre para pousar
        resultado = self._status.solicitarPouso()
        self.alterarStatus(resultado.estado)
        return resultado.mensagem

    def solicitarDecolagem(self):  # pedido da aeronave para a torre para decolagem
        if self._planoVoo is None:
            print("ALERT: defina o plano de voo antes da decolagem.")
            return ""
        resultado = self._status.solicitarDecolagem()
        self.alterarStatus(resultado.estado)
        return resultado.mensagem

    def pousar(self):  # informando a torre que esta pousando
        resultado = self._status.pousar()
        self.alterarStatus(resultado.estado)
        return resultado.mensagem

    def decolar(self):  # informando a torre que esta decolando
        resultado = self._status.decolar()
        self.alterarStatus(resultado.estado)
        return resultado.mensagem

    def declararEmergencia(
        self,
    ):  # informa a torre que a aeronave está em estado de emergencia e necessita de prioridade
        resultado = self._status.declararEmergencia()
        self.alterarStatus(resultado.estado)
        return resultado.mensagem

    def __str__(ABC):
        pass
