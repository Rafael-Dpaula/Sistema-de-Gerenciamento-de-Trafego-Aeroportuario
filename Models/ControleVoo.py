from Models.Avioes.Aviao import Aviao
from Models.Observer.Observer import Observer


class ControleVoo(Observer):  # classe singleton que controla o observer
    __instancia = None  # variavel que armazena se ele possui uma instancia da classe
    __inicializado = (
        False  # variavel que indica se já foi criada uma instancia da classe
    )

    def __new__(cls):
        if ControleVoo.__instancia is None:  # verifica se ele já foi instanciado
            cls.__instancia = super().__new__(
                cls
            )  # cria uma instancia nova se ele ainda não foi instanciado
        return cls.__instancia

    def __init__(self):
        if (ControleVoo.__inicializado):  # verifica se o controle de voo já foi inicializado
            return  # impede a continuidade caso ele ja tenha sido inicializado antes

        self.__historicoContato: list[str] = []
        self.__aeronaves: list[Aviao] = []
        self.__filaPouso: list[Aviao] = []
        self.__filaDecolagem: list[Aviao] = []

        ControleVoo.__inicializado = True

    @property
    def historicoContato(self):
        return self.__historicoContato

    @property
    def aeronaves(self):
        return self.__aeronaves

    @property
    def filaPouso(self):
        return self.__filaPouso

    @property
    def filaDecolagem(self):
        return self.__filaDecolagem

    def atualizar(self, origem, notificacao):
        print(notificacao.mensagem)
        if (
            notificacao.estado.__name__ == "EmEmergencia"
        ):  # verifica se o aviao esta no estado de emergencia
            if origem in self.__filaPouso:  # testa se ele ja solicitou o pouso
                self.__filaPouso.remove(
                    origem
                )  # remove ele da fila de pouso para dar prioridade

            self.__filaPouso.insert(
                0, origem
            )  # coloca ele como prioridade maxima na fila de pouso

    def solicitarPouso(
        self, aviao: Aviao
    ):  # solicita para torre a permissao para pouso e adiciona o aviao na lista de espera para pousar
        if not isinstance(
            aviao, Aviao
        ):  # valida a instância para garantir que seja válida
            raise TypeError("ERROR: o objeto deve ser uma instância válida de Aviao.")
        if (
            aviao in self.__filaPouso
        ):  # verifica se o objeto Aviao já está na lista de pouso
            print(
                f"ALERT: a aeronave {aviao.identificador} já está na lista de pouso do controle."
            )
            return
        return self.__filaPouso.append(aviao)

    def solicitarDecolagem(
        self, aviao: Aviao
    ):  # solicita para torre a permissao para decolar e adiciona o aviao na lista de espera para decolagem
        if not isinstance(
            aviao, Aviao
        ):  # valida a instância para garantir que seja válida
            raise TypeError("ERROR: o objeto deve ser uma instância válida de Aviao.")
        if (
            aviao in self.__filaDecolagem
        ):  # verifica se o objeto Aviao já está na lista de decolagem
            print(
                f"ALERT: a aeronave {aviao.identificador} já está na lista de decolagem do controle."
            )
            return
        return self.__filaDecolagem.append(aviao)

    def autorizarPouso(
        self, aviao: Aviao
    ):  # garante a autorizacao de pouso ao aviao e retira ele da fila de pouso
        if not isinstance(
            aviao, Aviao
        ):  # valida a instância para garantir que seja válida
            raise TypeError("ERROR: o objeto deve ser uma instância válida de Aviao.")
        if (
            not aviao in self.__filaPouso
        ):  # verifica se o objeto Aviao não está na lista de pouso
            print(
                f"ALERT: a aeronave {aviao.identificador} não está na lista de pouso do controle."
            )
            return
        return self.__filaPouso.remove(aviao)

    def autorizarDecolagem(
        self, aviao: Aviao
    ):  # solicita para torre a permissao para pouso e adiciona o aviao na lista de espera para pousar
        if not isinstance(
            aviao, Aviao
        ):  # valida a instância para garantir que seja válida
            raise TypeError("ERROR: o objeto deve ser uma instância válida de Aviao.")
        if (
            not aviao in self.__filaDecolagem
        ):  # verifica se o objeto Aviao já está na lista de pouso
            print(
                f"ALERT: a aeronave {aviao.identificador} não está na lista de decolagem do controle."
            )
            return
        return self.__filaDecolagem.remove(aviao)

    def adicionarAeronave(
        self, aviao: Aviao
    ):  # adiciona uma aeronave a lista de aeronaves do controle de voo
        if not isinstance(aviao, Aviao):  # valida se a aeronave é uma instancia válida
            raise TypeError("ERROR: o objeto deve ser uma instância válida de Aviao")
        if aviao in self.__aeronaves:  # busca se a aeronava já está na lista
            print(
                f"ALERT: a aeronave {aviao.identificador} já está na lista de aeronaves do controle"
            )
            return
        return self.__aeronaves.append(aviao)  # adiciona a aeronave da lista

    def removerAeronave(
        self, aviao: Aviao
    ):  # remove uma aeronave da lista de aeronaves do controle de voo
        if not isinstance(aviao, Aviao):  # valida se a aeronave é uma instancia válida
            raise TypeError("ERROR: o objeto deve ser uma instância válida de Aviao")
        if aviao not in self.__aeronaves:  # busca se a aeronava está na lista
            print(
                f"ALERT: a aeronave {aviao.identificador} não se encontra na lista de aeronaves do controle"
            )
            self.__aeronaves.remove(aviao)
