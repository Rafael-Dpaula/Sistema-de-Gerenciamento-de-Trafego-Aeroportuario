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
        if not (ControleVoo.__inicializado):
            self._historicoContato: list[str] = []
            self._aeronaves: list[Aviao] = []
            self._filaPouso: list[Aviao] = []
            self._filaDecolagem: list[Aviao] = []
            ControleVoo.__inicializado = True

    @property
    def historicoContato(self):
        return self._historicoContato

    @property
    def aeronaves(self):
        return self._aeronaves

    @property
    def filaPouso(self):
        return self._filaPouso

    @property
    def filaDecolagem(self):
        return self._filaDecolagem

    def __eq__(self, controle: ControleVoo):
        if self is controle and isinstance(controle, ControleVoo):
            return True
        return False

    def atualizar(self, origem, notificacao):
        self._historicoContato.append(notificacao)
        print(notificacao)
        if (
            type(origem._status).__name__.lower() == "ememergencia"
        ):  # verifica se o aviao esta no estado de emergencia
            if origem in self._filaPouso:  # testa se ele ja solicitou o pouso
                self._filaPouso.remove(
                    origem
                )  # remove ele da fila de pouso para dar prioridade

            self._filaPouso.insert(
                0, origem
            )  # coloca ele como prioridade maxima na fila de pouso

    # segunda ação de contato, coloca a aeronave na lista de pouso
    def solicitarPouso(
        self, aviao: Aviao
    ):  # solicita para torre a permissao para pouso e adiciona o aviao na lista de espera para pousar
        if not isinstance(
            aviao, Aviao
        ):  # valida a instância para garantir que seja válida
            raise TypeError("ERROR: o objeto deve ser uma instância válida de Aviao.")
        if (
            aviao in self._filaPouso
        ):  # verifica se o objeto Aviao já está na lista de pouso

            print(
                f"ALERT: a aeronave {aviao.identificador} já está na lista de pouso do controle."
            )
            return
        print(f"Controle → {aviao._identificador}: Pouso solicitado.")
        return self._filaPouso.append(aviao)

    # segunda ação de contato, coloca a aeronave na lista de decolagem
    def solicitarDecolagem(
        self, aviao: Aviao
    ):  # solicita para torre a permissao para decolar e adiciona o aviao na lista de espera para decolagem
        if not isinstance(
            aviao, Aviao
        ):  # valida a instância para garantir que seja válida
            raise TypeError("ERROR: o objeto deve ser uma instância válida de Aviao.")
        if (
            aviao in self._filaDecolagem
        ):  # verifica se o objeto Aviao já está na lista de decolagem

            print(
                f"ALERT: a aeronave {aviao.identificador} já está na lista de decolagem do controle."
            )
            return
        print(f"Controle → {aviao._identificador}: Decolagem solicitada.")
        return self._filaDecolagem.append(aviao)

    def autorizarPouso(self, aviao: Aviao):
        if not isinstance(aviao, Aviao):
            raise TypeError("ERROR: o objeto deve ser uma instância válida de Aviao.")
        if aviao not in self._filaPouso:
            print(
                f"ALERT: a aeronave {aviao.identificador} não está na lista de pouso do controle."
            )
            return
        if self._filaPouso[0] != aviao:
            print(
                f"ALERT: a aeronave {aviao.identificador} não é a primeira da fila de pouso."
            )
            return
        self._filaPouso.pop(0)

    def autorizarDecolagem(self, aviao: Aviao):
        if not isinstance(aviao, Aviao):
            raise TypeError("ERROR: o objeto deve ser uma instância válida de Aviao.")
        if aviao not in self._filaDecolagem:
            print(
                f"ALERT: a aeronave {aviao.identificador} não está na lista de decolagem do controle."
            )
            return
        if self._filaDecolagem[0] != aviao:
            print(
                f"ALERT: a aeronave {aviao.identificador} não é a primeira da fila de decolagem."
            )
            return
        self._filaDecolagem.pop(0)

    def adicionarAeronave(
        self, aviao: Aviao
    ):  # adiciona uma aeronave a lista de aeronaves do controle de voo
        if not isinstance(aviao, Aviao):  # valida se a aeronave é uma instancia válida
            raise TypeError("ERROR: o objeto deve ser uma instância válida de Aviao")
        if aviao in self._aeronaves:  # busca se a aeronava já está na lista

            print(
                f"ALERT: a aeronave {aviao.identificador} já está na lista de aeronaves do controle"
            )
            return
        return self._aeronaves.append(aviao)  # adiciona a aeronave da lista

    def removerAeronave(
        self, aviao: Aviao
    ):  # remove uma aeronave da lista de aeronaves do controle de voo
        if not isinstance(aviao, Aviao):  # valida se a aeronave é uma instancia válida
            raise TypeError("ERROR: o objeto deve ser uma instância válida de Aviao")
        if aviao not in self._aeronaves:  # busca se a aeronava está na lista

            print(
                f"ALERT: a aeronave {aviao.identificador} não se encontra na lista de aeronaves do controle"
            )
            self._aeronaves.remove(aviao)

    def __str__(self):
        return f"===== CONTROLE DE VOO =====\nHistorico de contato: {[h for h in self._historicoContato]}\nAeronaves: {[a._identificador for a in self._aeronaves]}\nFila de Pouso: {[fp._identificador for fp in self._filaPouso]}\nFila de Decolagem: {[fd._identificador for fd in self._filaDecolagem]}\n==========================="
