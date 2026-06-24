from Models.Aeroporto import Aeroporto
from Models.ControleVoo import ControleVoo
from Models.Avioes.Aviao import Aviao


class CentroOperacional:
    def __init__(self, aeroporto: Aeroporto, controleVoo: ControleVoo):
        self.aeroporto = aeroporto
        self.controleVoo = controleVoo

    @property
    def aeroporto(self):
        return self._aeroporto

    @property
    def controleVoo(self):
        return self._controleVoo

    @aeroporto.setter
    def aeroporto(self, novoAero):
        if not isinstance(novoAero, Aeroporto):
            raise ValueError("ERROR: novoAero não é uma instância válida de Aeroporto.")
        self._aeroporto = novoAero

    @controleVoo.setter
    def controleVoo(self, novoControle):
        if not isinstance(novoControle, ControleVoo):
            raise ValueError(
                "ERROR: novoControle não é uma instância válida de ControleVoo."
            )
        self._controleVoo = novoControle

    def autorizarPouso(self, aviao: Aviao):
        if type(aviao._status).__name__.lower() == "emsolo":
            return
        if aviao not in self._controleVoo.filaPouso:
            print(
                f"ALERT: a aeronave {aviao._identificador} não está na fila de pouso."
            )
            return
        if self._controleVoo.filaPouso[0] != aviao:
            print(
                f"ALERT: a aeronave {aviao._identificador} não é a primeira da fila de pouso."
            )
            return
        pista = self._aeroporto.buscarPistaDisponivel()
        if any(p.aviao == aviao for p in self._aeroporto.plataformas):
            print("ALERT: o avião já se encontra em uma plataforma.")
            return
        if pista is None:
            print("ALERT: não existem pistas disponíveis.")
            return
        pista.ocupar(aviao)
        self._controleVoo.autorizarPouso(aviao)
        print(aviao.pousar())
        print(
            f"Controle → {aviao._identificador}: Pouso autorizado e pista liberada. Desça com cuidado!"
        )
        return pista

    def autorizarDecolagem(self, aviao: Aviao):
        if aviao._planoVoo is None:
            return
        if aviao not in self._controleVoo.filaDecolagem:
            print(
                f"ALERT: a aeronave {aviao._identificador} não está na fila de decolagem."
            )
            return
        if self._controleVoo.filaDecolagem[0] != aviao:
            print(
                f"ALERT: a aeronave {aviao._identificador} não possui prioridade para decolagem."
            )
            return
        pista = self._aeroporto.buscarPistaDisponivel()
        if pista is None:
            print("ALERT: não existem pistas disponíveis.")
            return
        plataformaUtilizada = None
        for plataforma in self._aeroporto._plataformas:
            if plataforma.aviao == aviao:
                plataformaUtilizada = plataforma
                break
        if plataformaUtilizada is None:
            print("ALERT: aeronave não está ocupando nenhuma plataforma.")
            return
        plataformaUtilizada.liberar()
        pista.ocupar(aviao)
        self._controleVoo.autorizarDecolagem(aviao)
        print(aviao.decolar())
        print(
            f"Controle → {aviao._identificador}: Decolagem autorizada. Taxeie até a pista reservada."
        )
        return pista

    def processarPouso(self, aviao: Aviao):
        if any(p.aviao == aviao for p in self._aeroporto.plataformas):
            print("ALERT: o avião já se encontra em uma plataforma.")
            return
        pistaUtilizada = None
        for pista in self._aeroporto._pistas:
            if pista._aviao == aviao:
                pistaUtilizada = pista
                break
        if pistaUtilizada is None:
            print("ALERT: aeronave não está ocupando nenhuma pista.")
            return
        if self._controleVoo.filaPouso[0] != aviao:
            print(
                f"ALERT: a aeronave {aviao._identificador} não é a primeira da fila de pouso."
            )
            return
        plataforma = self._aeroporto.buscarPlataformaDisponivel()
        if plataforma is None:
            print("ALERT: não existem plataformas disponíveis.")
            return
        print(aviao.pousar())
        plataforma.ocupar(aviao)
        print(
            f"Controle → {aviao._identificador}: Excelente pouso! Plataforma reservada, taxeie até o destino."
        )
        pistaUtilizada.liberar()
        self._controleVoo.filaPouso.pop(0)

    def processarDecolagem(self, aviao: Aviao):
        if aviao is None or not isinstance(aviao, Aviao):
            raise ValueError("ERROR: aviao não é uma instância válida de Aviao.")
        if self._controleVoo.filaDecolagem[0] != aviao:
            print(
                f"ALERT: a aeronave {aviao._identificador} não é a primeira da fila de Decolagem."
            )
            return
        pistaUtilizada = None
        for pista in self._aeroporto._pistas:
            if pista._aviao == aviao:
                pistaUtilizada = pista
                break
        if pistaUtilizada is None:
            print("ALERT: aeronave não está ocupando nenhuma pista.")
            return
        print(aviao.decolar())
        print(
            f"Controle → {aviao._identificador}: Excelente decolagem. Tenha um bom voo!"
        )
        pistaUtilizada.liberar()
        self._controleVoo.filaDecolagem.pop(0)

    def processarEmergencia(self, aviao: Aviao):
        if aviao is None or not isinstance(aviao, Aviao):
            raise ValueError("ERROR: aviao não é uma instância válida de Aviao.")
        stateAnterior = type(aviao._status).__name__.upper()
        print(stateAnterior)
        print(aviao.declararEmergencia())
        if stateAnterior == "DECOLANDO":
            pistaUtilizada = None
            for pista in self._aeroporto._pistas:
                if pista._aviao == aviao:
                    pistaUtilizada = pista
                    break
            pistaUtilizada.liberar()
            plataforma = self._aeroporto.buscarPlataformaDisponivel()
            plataforma.ocupar(aviao)
            print(
                f"Controle → {aviao._identificador}: taxeie para a plataforma livre mais próxima, enviaremos suporte de imediato."
            )
            return
        elif stateAnterior == "EMSOLO":
            print(
                f"Controle → {aviao._identificador}: Mantenha-se na plataforma, o suporte está a caminho."
            )
        elif stateAnterior == "SOLICITANDOPOUSO":
            pista = self._aeroporto.buscarPistaDisponivel()
            if pista is None:
                pista = self._aeroporto._pistas[0]
                aviaoAnterior = pista._aviao
                if aviaoAnterior is not None:
                    print(
                        f"Emergência: removendo {aviaoAnterior._identificador} da pista {pista._codigo}"
                    )
                    pista.liberar()
            pista.ocupar(aviao)
            print(
                f"Controle → {aviao._identificador}: emergência recebida. Pista {pista._codigo} reservada com prioridade máxima."
            )

    def __str__(self):
        return f"===== CENTRO OPERACIONAL =====\n{self._aeroporto.__str__()}\n{self._controleVoo.__str__()}\n=============================="
